#!/usr/bin/env python3
"""
Backend API Testing for N&N Makeup Academy
Tests authentication, courses, live classes, and my-courses endpoints
"""

import requests
import json
import sys
from datetime import datetime

# Backend URL from frontend .env
BACKEND_URL = "https://makeupacademy.preview.emergentagent.com/api"

class BackendTester:
    def __init__(self):
        self.session = requests.Session()
        self.auth_token = None
        self.test_phone = "9876543210"
        self.results = {
            "auth_flow": {"status": "pending", "details": []},
            "courses_api": {"status": "pending", "details": []},
            "live_classes": {"status": "pending", "details": []},
            "my_courses": {"status": "pending", "details": []}
        }
    
    def log_result(self, category, message, success=True):
        """Log test result"""
        status = "✅" if success else "❌"
        print(f"{status} {category}: {message}")
        self.results[category]["details"].append({
            "message": message,
            "success": success,
            "timestamp": datetime.now().isoformat()
        })
    
    def test_auth_flow(self):
        """Test authentication flow: send OTP -> verify OTP"""
        print("\n=== Testing Authentication Flow ===")
        
        try:
            # Step 1: Send OTP
            print(f"1. Sending OTP to {self.test_phone}...")
            response = self.session.post(
                f"{BACKEND_URL}/auth/send-otp",
                json={"phone": self.test_phone},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code != 200:
                self.log_result("auth_flow", f"Send OTP failed: {response.status_code} - {response.text}", False)
                self.results["auth_flow"]["status"] = "failed"
                return False
            
            otp_data = response.json()
            if not otp_data.get("success"):
                self.log_result("auth_flow", f"Send OTP response invalid: {otp_data}", False)
                self.results["auth_flow"]["status"] = "failed"
                return False
            
            # Extract OTP from response (development mode)
            otp = otp_data.get("otp")
            if not otp:
                self.log_result("auth_flow", "OTP not found in response", False)
                self.results["auth_flow"]["status"] = "failed"
                return False
            
            self.log_result("auth_flow", f"OTP sent successfully: {otp}")
            
            # Step 2: Verify OTP
            print(f"2. Verifying OTP: {otp}...")
            response = self.session.post(
                f"{BACKEND_URL}/auth/verify-otp",
                json={"phone": self.test_phone, "otp": otp},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code != 200:
                self.log_result("auth_flow", f"Verify OTP failed: {response.status_code} - {response.text}", False)
                self.results["auth_flow"]["status"] = "failed"
                return False
            
            verify_data = response.json()
            if not verify_data.get("success"):
                self.log_result("auth_flow", f"Verify OTP response invalid: {verify_data}", False)
                self.results["auth_flow"]["status"] = "failed"
                return False
            
            # Extract token
            self.auth_token = verify_data.get("token")
            if not self.auth_token:
                self.log_result("auth_flow", "Token not found in verify response", False)
                self.results["auth_flow"]["status"] = "failed"
                return False
            
            self.log_result("auth_flow", f"Authentication successful, token: {self.auth_token[:10]}...")
            self.results["auth_flow"]["status"] = "passed"
            return True
            
        except Exception as e:
            self.log_result("auth_flow", f"Authentication flow error: {str(e)}", False)
            self.results["auth_flow"]["status"] = "failed"
            return False
    
    def test_courses_api(self):
        """Test courses API endpoints - Focus on 9 new small courses"""
        print("\n=== Testing Courses API (9 New Small Courses) ===")
        
        try:
            # Test GET /api/courses
            print("1. Testing GET /api/courses...")
            response = self.session.get(f"{BACKEND_URL}/courses")
            
            if response.status_code != 200:
                self.log_result("courses_api", f"GET courses failed: {response.status_code} - {response.text}", False)
                self.results["courses_api"]["status"] = "failed"
                return False
            
            courses = response.json()
            if not isinstance(courses, list):
                self.log_result("courses_api", f"Courses response not a list: {type(courses)}", False)
                self.results["courses_api"]["status"] = "failed"
                return False
            
            # Should have more than the original 3 courses now
            if len(courses) < 4:
                self.log_result("courses_api", f"Expected more than 3 courses (original + 9 new), got {len(courses)}", False)
                self.results["courses_api"]["status"] = "failed"
                return False
            
            self.log_result("courses_api", f"GET courses successful: {len(courses)} courses returned (expected >3)")
            
            # Check for expected new courses
            expected_new_courses = [
                "Basic Eyebrow Shaping",
                "Everyday Natural Makeup", 
                "Festive Glam",
                "Nail Care & Polish Basics",
                "Beginner Nail Art", 
                "Gel Nail Application",
                "Everyday Hairstyling",
                "Quick Bridal Hairstyles",
                "Heatless Curls"
            ]
            
            print("\n2. Checking for new small courses...")
            found_new_courses = []
            course_details = []
            
            for course in courses:
                title = course.get('title', '')
                category = course.get('category', '')
                price_inr = course.get('price_inr')
                
                # Check if this matches any expected new course
                for expected in expected_new_courses:
                    if any(word.lower() in title.lower() for word in expected.split()):
                        found_new_courses.append(title)
                        course_details.append({
                            'title': title,
                            'category': category, 
                            'price_inr': price_inr,
                            'id': course.get('id')
                        })
                        break
            
            print(f"Found {len(found_new_courses)} new courses:")
            for detail in course_details:
                print(f"  - {detail['title']} ({detail['category']}) - ₹{detail['price_inr']}")
            
            if len(found_new_courses) < 5:
                self.log_result("courses_api", f"Expected to find more new courses, only found {len(found_new_courses)}", False)
                self.results["courses_api"]["status"] = "failed"
                return False
            
            # Test GET /api/courses/{id} for one of the new small courses
            if course_details:
                test_course = course_details[0]  # Test first new course found
                course_id = test_course['id']
                
                print(f"\n3. Testing GET /api/courses/{course_id} for '{test_course['title']}'...")
                response = self.session.get(f"{BACKEND_URL}/courses/{course_id}")
                
                if response.status_code != 200:
                    self.log_result("courses_api", f"GET course by ID failed: {response.status_code} - {response.text}", False)
                    self.results["courses_api"]["status"] = "failed"
                    return False
                
                course = response.json()
                
                # Verify required fields for new courses
                required_fields = ['title', 'description', 'price', 'category', 'instructor', 'duration']
                missing_fields = [field for field in required_fields if not course.get(field)]
                
                if missing_fields:
                    self.log_result("courses_api", f"Course missing required fields: {missing_fields}", False)
                    self.results["courses_api"]["status"] = "failed"
                    return False
                
                # Check for price_inr field (critical for new courses)
                if 'price_inr' not in course:
                    self.log_result("courses_api", "New course missing price_inr field", False)
                    self.results["courses_api"]["status"] = "failed"
                    return False
                
                self.log_result("courses_api", f"Course details verified: {course.get('title')} - ₹{course.get('price_inr')}")
                
                # Check lessons structure
                lessons = course.get('lessons', [])
                if len(lessons) == 0:
                    self.log_result("courses_api", "Warning: Course has no lessons", False)
                else:
                    self.log_result("courses_api", f"Course has {len(lessons)} lessons/sections")
                    
                    # Check if lessons contain structured data
                    has_structured_content = False
                    for lesson in lessons:
                        if isinstance(lesson, dict) and len(lesson) > 1:
                            has_structured_content = True
                            break
                    
                    if has_structured_content:
                        self.log_result("courses_api", "Course contains structured lesson content")
                    else:
                        self.log_result("courses_api", "Warning: Lessons may lack detailed structure", False)
            
            # Verify course categories
            print("\n4. Verifying course categories...")
            category_counts = {'makeup': 0, 'nail': 0, 'hair': 0}
            
            for detail in course_details:
                category = detail['category'].lower()
                if category in category_counts:
                    category_counts[category] += 1
            
            print(f"Category distribution: Makeup: {category_counts['makeup']}, Nail: {category_counts['nail']}, Hair: {category_counts['hair']}")
            
            # Should have courses in multiple categories
            active_categories = sum(1 for count in category_counts.values() if count > 0)
            if active_categories < 2:
                self.log_result("courses_api", f"Expected courses in multiple categories, found {active_categories}", False)
                self.results["courses_api"]["status"] = "failed"
                return False
            
            self.log_result("courses_api", f"New courses properly distributed across {active_categories} categories")
            
            self.results["courses_api"]["status"] = "passed"
            return True
            
        except Exception as e:
            self.log_result("courses_api", f"Courses API error: {str(e)}", False)
            self.results["courses_api"]["status"] = "failed"
            return False
    
    def test_live_classes(self):
        """Test live classes API"""
        print("\n=== Testing Live Classes API ===")
        
        try:
            print("1. Testing GET /api/live-classes...")
            response = self.session.get(f"{BACKEND_URL}/live-classes")
            
            if response.status_code != 200:
                self.log_result("live_classes", f"GET live classes failed: {response.status_code} - {response.text}", False)
                self.results["live_classes"]["status"] = "failed"
                return False
            
            live_classes = response.json()
            if not isinstance(live_classes, list):
                self.log_result("live_classes", f"Live classes response not a list: {type(live_classes)}", False)
                self.results["live_classes"]["status"] = "failed"
                return False
            
            self.log_result("live_classes", f"GET live classes successful: {len(live_classes)} classes returned")
            
            # Verify each class has required fields
            for i, lc in enumerate(live_classes):
                required_fields = ["id", "title", "description", "date_time", "instructor"]
                missing_fields = [field for field in required_fields if not lc.get(field)]
                if missing_fields:
                    self.log_result("live_classes", f"Class {i+1} missing fields: {missing_fields}", False)
                    self.results["live_classes"]["status"] = "failed"
                    return False
            
            self.results["live_classes"]["status"] = "passed"
            return True
            
        except Exception as e:
            self.log_result("live_classes", f"Live classes API error: {str(e)}", False)
            self.results["live_classes"]["status"] = "failed"
            return False
    
    def test_my_courses(self):
        """Test my courses API with authentication"""
        print("\n=== Testing My Courses API (with auth) ===")
        
        if not self.auth_token:
            self.log_result("my_courses", "No auth token available for testing", False)
            self.results["my_courses"]["status"] = "failed"
            return False
        
        try:
            print("1. Testing GET /api/my-courses with auth token...")
            headers = {"Authorization": f"Bearer {self.auth_token}"}
            response = self.session.get(f"{BACKEND_URL}/my-courses", headers=headers)
            
            if response.status_code != 200:
                self.log_result("my_courses", f"GET my courses failed: {response.status_code} - {response.text}", False)
                self.results["my_courses"]["status"] = "failed"
                return False
            
            my_courses = response.json()
            if not isinstance(my_courses, list):
                self.log_result("my_courses", f"My courses response not a list: {type(my_courses)}", False)
                self.results["my_courses"]["status"] = "failed"
                return False
            
            self.log_result("my_courses", f"GET my courses successful: {len(my_courses)} enrolled courses")
            
            # Test without auth token (should fail)
            print("2. Testing GET /api/my-courses without auth (should fail)...")
            response = self.session.get(f"{BACKEND_URL}/my-courses")
            
            if response.status_code == 200:
                self.log_result("my_courses", "My courses endpoint should require authentication", False)
                self.results["my_courses"]["status"] = "failed"
                return False
            
            self.log_result("my_courses", f"Correctly rejected unauthenticated request: {response.status_code}")
            
            self.results["my_courses"]["status"] = "passed"
            return True
            
        except Exception as e:
            self.log_result("my_courses", f"My courses API error: {str(e)}", False)
            self.results["my_courses"]["status"] = "failed"
            return False
    
    def run_all_tests(self):
        """Run all backend tests"""
        print(f"🚀 Starting Backend API Tests for N&N Makeup Academy")
        print(f"Backend URL: {BACKEND_URL}")
        print("=" * 60)
        
        # First, seed data if needed
        try:
            print("Seeding initial data...")
            response = self.session.post(f"{BACKEND_URL}/admin/seed-data")
            if response.status_code == 200:
                print("✅ Data seeded successfully")
            else:
                print(f"⚠️  Seed data response: {response.status_code}")
        except Exception as e:
            print(f"⚠️  Seed data error: {str(e)}")
        
        # Run tests in sequence
        tests = [
            ("Authentication Flow", self.test_auth_flow),
            ("Courses API", self.test_courses_api),
            ("Live Classes API", self.test_live_classes),
            ("My Courses API", self.test_my_courses)
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            if test_func():
                passed += 1
        
        # Print summary
        print("\n" + "=" * 60)
        print(f"🏁 Test Summary: {passed}/{total} tests passed")
        
        for category, result in self.results.items():
            status_icon = "✅" if result["status"] == "passed" else "❌" if result["status"] == "failed" else "⏳"
            print(f"{status_icon} {category.replace('_', ' ').title()}: {result['status']}")
        
        return passed == total

if __name__ == "__main__":
    tester = BackendTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)