from fastapi import FastAPI, APIRouter, HTTPException, Request, Header
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
import logging
import random
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
from emergentintegrations.payments.stripe.checkout import StripeCheckout, CheckoutSessionResponse, CheckoutStatusResponse, CheckoutSessionRequest
from twilio.rest import Client

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Stripe setup
STRIPE_API_KEY = os.environ['STRIPE_API_KEY']

# Twilio setup
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# ============= Models =============

class User(BaseModel):
    id: Optional[str] = None
    phone: str
    name: Optional[str] = None
    email: Optional[str] = None
    enrolled_courses: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)

class PhoneRequest(BaseModel):
    phone: str

class OTPVerifyRequest(BaseModel):
    phone: str
    otp: str

class CourseLesson(BaseModel):
    id: str
    title: str
    description: str
    video_url: str
    duration: int  # in minutes
    order: int

class Course(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    price: float
    thumbnail: str
    category: str
    lessons: List[Dict[str, Any]] = []
    instructor: str
    duration: str
    students_count: int = 0

class LiveClass(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    date_time: datetime
    instructor: str
    max_participants: int
    enrolled_users: List[str] = []
    thumbnail: str
    duration: int  # in minutes

class Enrollment(BaseModel):
    id: Optional[str] = None
    user_id: str
    course_id: str
    progress: float = 0.0
    completed_lessons: List[str] = []
    enrolled_at: datetime = Field(default_factory=datetime.utcnow)

class PaymentTransaction(BaseModel):
    id: Optional[str] = None
    user_id: str
    course_id: str
    amount: float
    currency: str
    session_id: str
    payment_status: str = "pending"
    metadata: Optional[Dict[str, str]] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class CheckoutRequest(BaseModel):
    course_id: str
    origin_url: str

class ProgressUpdate(BaseModel):
    lesson_id: str

class LiveClassBooking(BaseModel):
    class_id: str

# ============= Helper Functions =============

def serialize_doc(doc):
    """Convert MongoDB document to JSON-serializable format"""
    if doc and '_id' in doc:
        doc['id'] = str(doc['_id'])
        del doc['_id']
    return doc

# Generate mock OTP (in production, use Twilio or similar)
OTP_STORAGE = {}

def generate_otp():
    return str(random.randint(100000, 999999))

# ============= Authentication APIs =============

@api_router.post("/auth/send-otp")
async def send_otp(request: PhoneRequest):
    """Send OTP to phone number via Twilio SMS"""
    otp = generate_otp()
    OTP_STORAGE[request.phone] = otp
    
    # Format phone number for Twilio (add +91 prefix for Indian numbers)
    phone_number = request.phone
    if not phone_number.startswith('+'):
        phone_number = f"+91{phone_number}"
    
    try:
        # Send SMS via Twilio
        message = twilio_client.messages.create(
            body=f"Your N&N Makeup Academy OTP is: {otp}. Valid for 10 minutes.",
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        
        logging.info(f"SMS sent to {phone_number}. Message SID: {message.sid}")
        logging.info(f"OTP for {request.phone}: {otp}")
        
        return {
            "success": True,
            "message": "OTP sent successfully to your phone",
            "otp": otp  # Keep this for development/testing
        }
    except Exception as e:
        logging.error(f"Failed to send SMS to {phone_number}: {str(e)}")
        # Still return success but with warning
        return {
            "success": True,
            "message": "OTP generated (SMS service unavailable)",
            "otp": otp,
            "warning": "Please use the OTP shown on screen"
        }

@api_router.post("/auth/verify-otp")
async def verify_otp(request: OTPVerifyRequest):
    """Verify OTP and create/login user"""
    stored_otp = OTP_STORAGE.get(request.phone)
    
    if not stored_otp or stored_otp != request.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")
    
    # Remove used OTP
    del OTP_STORAGE[request.phone]
    
    # Check if user exists
    user = await db.users.find_one({"phone": request.phone})
    
    if not user:
        # Create new user
        new_user = {
            "phone": request.phone,
            "name": None,
            "email": None,
            "enrolled_courses": [],
            "created_at": datetime.utcnow()
        }
        result = await db.users.insert_one(new_user)
        new_user['_id'] = result.inserted_id
        user = new_user
    
    user = serialize_doc(user)
    
    return {
        "success": True,
        "message": "Login successful",
        "user": user,
        "token": user['id']  # Simple token (use JWT in production)
    }

@api_router.get("/auth/me")
async def get_current_user(authorization: Optional[str] = Header(None)):
    """Get current user details"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = authorization.replace("Bearer ", "")
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return serialize_doc(user)

@api_router.put("/auth/profile")
async def update_profile(
    name: Optional[str] = None,
    email: Optional[str] = None,
    authorization: Optional[str] = Header(None)
):
    """Update user profile"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = authorization.replace("Bearer ", "")
    update_data = {}
    
    if name:
        update_data['name'] = name
    if email:
        update_data['email'] = email
    
    await db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )
    
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    return serialize_doc(user)

# ============= Course APIs =============

@api_router.get("/courses")
async def get_courses(category: Optional[str] = None):
    """Get all courses or filter by category"""
    query = {}
    if category:
        query['category'] = category
    
    courses = await db.courses.find(query).to_list(100)
    return [serialize_doc(course) for course in courses]

@api_router.get("/courses/{course_id}")
async def get_course(course_id: str):
    """Get course details"""
    course = await db.courses.find_one({"_id": ObjectId(course_id)})
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return serialize_doc(course)

@api_router.get("/my-courses")
async def get_my_courses(authorization: Optional[str] = Header(None)):
    """Get user's enrolled courses"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = authorization.replace("Bearer ", "")
    
    # Get enrollments
    enrollments = await db.enrollments.find({"user_id": user_id}).to_list(100)
    
    # Get course details
    result = []
    for enrollment in enrollments:
        course = await db.courses.find_one({"_id": ObjectId(enrollment['course_id'])})
        if course:
            course = serialize_doc(course)
            course['progress'] = enrollment.get('progress', 0.0)
            course['enrollment_id'] = str(enrollment['_id'])
            result.append(course)
    
    return result

@api_router.post("/courses/{course_id}/progress")
async def update_progress(
    course_id: str,
    request: ProgressUpdate,
    authorization: Optional[str] = Header(None)
):
    """Update lesson progress"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = authorization.replace("Bearer ", "")
    
    # Find enrollment
    enrollment = await db.enrollments.find_one({
        "user_id": user_id,
        "course_id": course_id
    })
    
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    
    # Add lesson to completed if not already there
    completed_lessons = enrollment.get('completed_lessons', [])
    if request.lesson_id not in completed_lessons:
        completed_lessons.append(request.lesson_id)
    
    # Calculate progress
    course = await db.courses.find_one({"_id": ObjectId(course_id)})
    if course:
        total_lessons = len(course.get('lessons', []))
        progress = (len(completed_lessons) / total_lessons * 100) if total_lessons > 0 else 0
        
        await db.enrollments.update_one(
            {"_id": enrollment['_id']},
            {
                "$set": {
                    "completed_lessons": completed_lessons,
                    "progress": progress
                }
            }
        )
        
        return {"success": True, "progress": progress}
    
    return {"success": False}

# ============= Payment APIs =============

@api_router.post("/payment/create-checkout")
async def create_checkout(
    request: CheckoutRequest,
    http_request: Request,
    authorization: Optional[str] = Header(None)
):
    """Create Stripe checkout session"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = authorization.replace("Bearer ", "")
    
    # Get course details
    course = await db.courses.find_one({"_id": ObjectId(request.course_id)})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Check if already enrolled
    existing_enrollment = await db.enrollments.find_one({
        "user_id": user_id,
        "course_id": request.course_id
    })
    
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Already enrolled in this course")
    
    # Create webhook URL
    host_url = str(http_request.base_url).rstrip('/')
    webhook_url = f"{host_url}/api/webhook/stripe"
    
    # Initialize Stripe
    stripe_checkout = StripeCheckout(api_key=STRIPE_API_KEY, webhook_url=webhook_url)
    
    # Create success and cancel URLs
    success_url = f"{request.origin_url}/payment-success?session_id={{{{CHECKOUT_SESSION_ID}}}}"
    cancel_url = f"{request.origin_url}/courses/{request.course_id}"
    
    # Create checkout session
    checkout_request = CheckoutSessionRequest(
        amount=float(course['price']),
        currency="usd",
        success_url=success_url,
        cancel_url=cancel_url,
        metadata={
            "user_id": user_id,
            "course_id": request.course_id,
            "course_title": course['title']
        }
    )
    
    session = await stripe_checkout.create_checkout_session(checkout_request)
    
    # Store payment transaction
    transaction = {
        "user_id": user_id,
        "course_id": request.course_id,
        "amount": float(course['price']),
        "currency": "usd",
        "session_id": session.session_id,
        "payment_status": "pending",
        "metadata": checkout_request.metadata,
        "created_at": datetime.utcnow()
    }
    
    await db.payment_transactions.insert_one(transaction)
    
    return {
        "url": session.url,
        "session_id": session.session_id
    }

@api_router.get("/payment/status/{session_id}")
async def get_payment_status(session_id: str, authorization: Optional[str] = Header(None)):
    """Get payment status and enroll user if successful"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = authorization.replace("Bearer ", "")
    
    # Get transaction
    transaction = await db.payment_transactions.find_one({"session_id": session_id})
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    # If already completed, return status
    if transaction.get('payment_status') == 'paid':
        return {"status": "success", "message": "Payment already processed"}
    
    # Check with Stripe
    stripe_checkout = StripeCheckout(api_key=STRIPE_API_KEY, webhook_url="")
    checkout_status = await stripe_checkout.get_checkout_status(session_id)
    
    # Update transaction
    await db.payment_transactions.update_one(
        {"session_id": session_id},
        {
            "$set": {
                "payment_status": checkout_status.payment_status,
                "status": checkout_status.status
            }
        }
    )
    
    # If payment successful and not already enrolled, create enrollment
    if checkout_status.payment_status == "paid":
        existing_enrollment = await db.enrollments.find_one({
            "user_id": transaction['user_id'],
            "course_id": transaction['course_id']
        })
        
        if not existing_enrollment:
            enrollment = {
                "user_id": transaction['user_id'],
                "course_id": transaction['course_id'],
                "progress": 0.0,
                "completed_lessons": [],
                "enrolled_at": datetime.utcnow()
            }
            await db.enrollments.insert_one(enrollment)
            
            # Update course students count
            await db.courses.update_one(
                {"_id": ObjectId(transaction['course_id'])},
                {"$inc": {"students_count": 1}}
            )
            
            # Update user's enrolled courses
            await db.users.update_one(
                {"_id": ObjectId(transaction['user_id'])},
                {"$addToSet": {"enrolled_courses": transaction['course_id']}}
            )
        
        return {"status": "success", "message": "Payment successful, enrollment created"}
    
    return {"status": checkout_status.status, "payment_status": checkout_status.payment_status}

@api_router.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    """Handle Stripe webhooks"""
    try:
        body = await request.body()
        signature = request.headers.get("Stripe-Signature")
        
        stripe_checkout = StripeCheckout(api_key=STRIPE_API_KEY, webhook_url="")
        webhook_response = await stripe_checkout.handle_webhook(body, signature)
        
        logging.info(f"Webhook received: {webhook_response.event_type}")
        
        return {"status": "success"}
    except Exception as e:
        logging.error(f"Webhook error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

# ============= Live Classes APIs =============

@api_router.get("/live-classes")
async def get_live_classes():
    """Get all upcoming live classes"""
    current_time = datetime.utcnow()
    live_classes = await db.live_classes.find({
        "date_time": {"$gte": current_time}
    }).sort("date_time", 1).to_list(100)
    
    return [serialize_doc(lc) for lc in live_classes]

@api_router.post("/live-classes/book")
async def book_live_class(
    request: LiveClassBooking,
    authorization: Optional[str] = Header(None)
):
    """Book a live class"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = authorization.replace("Bearer ", "")
    
    # Get live class
    live_class = await db.live_classes.find_one({"_id": ObjectId(request.class_id)})
    if not live_class:
        raise HTTPException(status_code=404, detail="Live class not found")
    
    # Check if already booked
    enrolled_users = live_class.get('enrolled_users', [])
    if user_id in enrolled_users:
        raise HTTPException(status_code=400, detail="Already booked this class")
    
    # Check capacity
    if len(enrolled_users) >= live_class['max_participants']:
        raise HTTPException(status_code=400, detail="Class is full")
    
    # Add user to enrolled users
    await db.live_classes.update_one(
        {"_id": ObjectId(request.class_id)},
        {"$addToSet": {"enrolled_users": user_id}}
    )
    
    return {"success": True, "message": "Class booked successfully"}

@api_router.get("/my-live-classes")
async def get_my_live_classes(authorization: Optional[str] = Header(None)):
    """Get user's booked live classes"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = authorization.replace("Bearer ", "")
    
    live_classes = await db.live_classes.find({
        "enrolled_users": user_id
    }).sort("date_time", 1).to_list(100)
    
    return [serialize_doc(lc) for lc in live_classes]

# ============= Admin/Seed APIs =============

@api_router.post("/admin/seed-data")
async def seed_data():
    """Seed initial data (courses and live classes)"""
    
    # Check if data already exists
    existing_courses = await db.courses.count_documents({})
    if existing_courses > 0:
        return {"message": "Data already seeded"}
    
    # Seed courses
    courses = [
        {
            "title": "Makeup Mastery",
            "description": "Master professional makeup skills from beginner to advanced level. Learn foundation techniques, contouring, eye makeup, and more.",
            "price": 49.99,
            "thumbnail": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400",
            "category": "makeup",
            "instructor": "Irfana Begum",
            "duration": "8 weeks",
            "students_count": 150,
            "lessons": [
                {
                    "id": "lesson1",
                    "title": "Introduction to Makeup",
                    "description": "Learn the basics of makeup and essential tools",
                    "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    "duration": 30,
                    "order": 1
                },
                {
                    "id": "lesson2",
                    "title": "Foundation & Base",
                    "description": "Master the art of perfect foundation application",
                    "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    "duration": 45,
                    "order": 2
                },
                {
                    "id": "lesson3",
                    "title": "Eye Makeup Techniques",
                    "description": "Create stunning eye looks with various techniques",
                    "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    "duration": 60,
                    "order": 3
                }
            ]
        },
        {
            "title": "Nail Artistry",
            "description": "Discover the art of nail design with specialized courses focusing on creativity, technique, and professional nail care.",
            "price": 39.99,
            "thumbnail": "https://images.unsplash.com/photo-1604654894610-df63bc536371?w=400",
            "category": "nail",
            "instructor": "Nausheen Khan",
            "duration": "6 weeks",
            "students_count": 89,
            "lessons": [
                {
                    "id": "lesson1",
                    "title": "Nail Care Basics",
                    "description": "Learn proper nail care and hygiene",
                    "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    "duration": 25,
                    "order": 1
                },
                {
                    "id": "lesson2",
                    "title": "Nail Art Techniques",
                    "description": "Create beautiful nail designs",
                    "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    "duration": 40,
                    "order": 2
                }
            ]
        },
        {
            "title": "Hair Styling Mastery",
            "description": "Enhance your skills with expert-led sessions covering hair styling techniques, updos, braiding, and professional salon practices.",
            "price": 44.99,
            "thumbnail": "https://images.unsplash.com/photo-1560066984-138dadb4c035?w=400",
            "category": "hair",
            "instructor": "Irfana Begum",
            "duration": "7 weeks",
            "students_count": 112,
            "lessons": [
                {
                    "id": "lesson1",
                    "title": "Hair Styling Basics",
                    "description": "Learn fundamental hair styling techniques",
                    "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    "duration": 35,
                    "order": 1
                },
                {
                    "id": "lesson2",
                    "title": "Braiding Techniques",
                    "description": "Master various braiding styles",
                    "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    "duration": 50,
                    "order": 2
                }
            ]
        }
    ]
    
    await db.courses.insert_many(courses)
    
    # Seed live classes
    live_classes = [
        {
            "title": "Bridal Makeup Workshop",
            "description": "Learn professional bridal makeup techniques in this interactive live session",
            "date_time": datetime.utcnow() + timedelta(days=3),
            "instructor": "Irfana Begum",
            "max_participants": 50,
            "enrolled_users": [],
            "thumbnail": "https://images.unsplash.com/photo-1487412947147-5cebf100ffc2?w=400",
            "duration": 120
        },
        {
            "title": "Nail Art Advanced Techniques",
            "description": "Advanced nail art workshop with live demonstrations",
            "date_time": datetime.utcnow() + timedelta(days=5),
            "instructor": "Nausheen Khan",
            "max_participants": 30,
            "enrolled_users": [],
            "thumbnail": "https://images.unsplash.com/photo-1610992015732-2449b76344bc?w=400",
            "duration": 90
        },
        {
            "title": "Hair Styling for Occasions",
            "description": "Create stunning hairstyles for special occasions",
            "date_time": datetime.utcnow() + timedelta(days=7),
            "instructor": "Irfana Begum",
            "max_participants": 40,
            "enrolled_users": [],
            "thumbnail": "https://images.unsplash.com/photo-1562322140-8baeececf3df?w=400",
            "duration": 100
        }
    ]
    
    await db.live_classes.insert_many(live_classes)
    
    return {"message": "Data seeded successfully"}

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
