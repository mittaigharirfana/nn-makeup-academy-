from fastapi import APIRouter
from fastapi.responses import HTMLResponse

policy_router = APIRouter()

@policy_router.get("/refund-policy", response_class=HTMLResponse)
async def refund_policy():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cancellation & Refund Policy - N&N Makeup Academy</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #FF1493; }
            h2 { color: #333; margin-top: 20px; }
            p { margin: 10px 0; }
        </style>
    </head>
    <body>
        <h1>Cancellation & Refund Policy</h1>
        <p><strong>N&N Makeup Academy</strong></p>
        <p>Last Updated: October 29, 2025</p>
        
        <h2>Cancellation Policy</h2>
        <p>Once you enroll in a course and make payment, you can cancel within 7 days of purchase for a full refund if you have not accessed more than 10% of the course content.</p>
        
        <h2>Refund Policy</h2>
        <p><strong>7-Day Money Back Guarantee:</strong> If you're not satisfied with the course within the first 7 days of purchase and have watched less than 10% of the videos, we will provide a full refund.</p>
        
        <p><strong>After 7 Days:</strong> No refunds will be provided after the 7-day period has elapsed.</p>
        
        <p><strong>Refund Process:</strong> Refunds will be processed within 7-10 business days after approval. The amount will be credited to the original payment method used during purchase.</p>
        
        <h2>How to Request a Refund</h2>
        <p>To request a refund, please contact us at:</p>
        <ul>
            <li>Email: support@nnmakeupandgrooming.com</li>
            <li>Phone: +91 9248444687</li>
            <li>WhatsApp: +91 9248444687</li>
        </ul>
        
        <h2>Non-Refundable Items</h2>
        <ul>
            <li>Courses purchased more than 7 days ago</li>
            <li>Courses where more than 10% content has been accessed</li>
            <li>Live class bookings (non-refundable after booking)</li>
        </ul>
        
        <p>For any questions about refunds, please contact our support team.</p>
    </body>
    </html>
    """

@policy_router.get("/terms-and-conditions", response_class=HTMLResponse)
async def terms_conditions():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Terms and Conditions - N&N Makeup Academy</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #FF1493; }
            h2 { color: #333; margin-top: 20px; }
            p { margin: 10px 0; }
        </style>
    </head>
    <body>
        <h1>Terms and Conditions</h1>
        <p><strong>N&N Makeup Academy</strong></p>
        <p>Last Updated: October 29, 2025</p>
        
        <h2>1. Acceptance of Terms</h2>
        <p>By accessing and using N&N Makeup Academy's services, you accept and agree to be bound by these Terms and Conditions.</p>
        
        <h2>2. Course Enrollment</h2>
        <p>Upon successful payment, you will receive immediate access to the enrolled course. All course materials are for personal use only and cannot be shared, distributed, or resold.</p>
        
        <h2>3. Payment</h2>
        <p>All course fees are listed in Indian Rupees (₹). Payment must be completed before accessing course content. We accept payments through credit/debit cards, UPI, net banking, and digital wallets via Razorpay.</p>
        
        <h2>4. Course Access</h2>
        <p>Once enrolled, you will have lifetime access to the course content unless otherwise specified. We reserve the right to modify or discontinue courses with prior notice.</p>
        
        <h2>5. Intellectual Property</h2>
        <p>All course content, including videos, text, images, and materials, are the intellectual property of N&N Makeup Academy. Unauthorized copying, distribution, or reproduction is prohibited.</p>
        
        <h2>6. User Conduct</h2>
        <p>Students agree not to:</p>
        <ul>
            <li>Share login credentials with others</li>
            <li>Download or redistribute course content</li>
            <li>Use content for commercial purposes without permission</li>
            <li>Engage in any activity that disrupts the platform</li>
        </ul>
        
        <h2>7. Limitation of Liability</h2>
        <p>N&N Makeup Academy is not liable for any indirect, incidental, or consequential damages arising from the use of our courses.</p>
        
        <h2>8. Contact Information</h2>
        <p>For questions about these Terms and Conditions, contact us at support@nnmakeupandgrooming.com</p>
    </body>
    </html>
    """

@policy_router.get("/shipping-policy", response_class=HTMLResponse)
async def shipping_policy():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shipping Policy - N&N Makeup Academy</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #FF1493; }
            h2 { color: #333; margin-top: 20px; }
            p { margin: 10px 0; }
        </style>
    </head>
    <body>
        <h1>Shipping Policy</h1>
        <p><strong>N&N Makeup Academy</strong></p>
        <p>Last Updated: October 29, 2025</p>
        
        <h2>Digital Products</h2>
        <p>N&N Makeup Academy offers <strong>digital online courses</strong> only. Since all our courses are delivered digitally through our online platform, there is no physical shipping involved.</p>
        
        <h2>Instant Access</h2>
        <p>Upon successful payment, you will receive <strong>immediate access</strong> to your enrolled course(s). No waiting period or shipping time is required.</p>
        
        <h2>Course Delivery</h2>
        <p>All course content including videos, study materials, and resources are accessible through:</p>
        <ul>
            <li>Our mobile application</li>
            <li>Web browser on any device</li>
            <li>Available 24/7 from anywhere with internet connection</li>
        </ul>
        
        <h2>Certificate Delivery</h2>
        <p>Upon course completion, certificates will be provided in <strong>digital format</strong> (PDF) and can be downloaded directly from your account. Physical certificates are not provided at this time.</p>
        
        <h2>Access Issues</h2>
        <p>If you experience any issues accessing your purchased course, please contact our support team immediately at support@nnmakeupandgrooming.com or +91 9248444687.</p>
    </body>
    </html>
    """

@policy_router.get("/privacy-policy", response_class=HTMLResponse)
async def privacy_policy():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Privacy Policy - N&N Makeup Academy</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #FF1493; }
            h2 { color: #333; margin-top: 20px; }
            p { margin: 10px 0; }
        </style>
    </head>
    <body>
        <h1>Privacy Policy</h1>
        <p><strong>N&N Makeup Academy</strong></p>
        <p>Last Updated: October 29, 2025</p>
        
        <h2>1. Information We Collect</h2>
        <p>We collect the following information when you use our services:</p>
        <ul>
            <li><strong>Personal Information:</strong> Name, email address, phone number</li>
            <li><strong>Payment Information:</strong> Processed securely through Razorpay (we do not store card details)</li>
            <li><strong>Usage Data:</strong> Course progress, lessons completed, login history</li>
        </ul>
        
        <h2>2. How We Use Your Information</h2>
        <p>Your information is used to:</p>
        <ul>
            <li>Provide access to courses and learning materials</li>
            <li>Process payments and send receipts</li>
            <li>Send course updates and important notifications</li>
            <li>Improve our services and user experience</li>
            <li>Provide customer support</li>
        </ul>
        
        <h2>3. Data Security</h2>
        <p>We implement industry-standard security measures to protect your personal information. All payment processing is handled through Razorpay's secure payment gateway.</p>
        
        <h2>4. Data Sharing</h2>
        <p>We do not sell, trade, or rent your personal information to third parties. We may share data with:</p>
        <ul>
            <li>Payment processors (Razorpay) for transaction processing</li>
            <li>Service providers who assist in operating our platform</li>
            <li>Legal authorities when required by law</li>
        </ul>
        
        <h2>5. Your Rights</h2>
        <p>You have the right to:</p>
        <ul>
            <li>Access your personal data</li>
            <li>Request corrections to your information</li>
            <li>Request deletion of your account and data</li>
            <li>Opt-out of marketing communications</li>
        </ul>
        
        <h2>6. Cookies</h2>
        <p>We use cookies to enhance user experience, remember login sessions, and analyze site usage. You can disable cookies in your browser settings.</p>
        
        <h2>7. Contact Us</h2>
        <p>For any privacy-related questions or concerns, contact us at:</p>
        <ul>
            <li>Email: support@nnmakeupandgrooming.com</li>
            <li>Phone: +91 9248444687</li>
        </ul>
    </body>
    </html>
    """

@policy_router.get("/contact-us", response_class=HTMLResponse)
async def contact_us():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Us - N&N Makeup Academy</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #FF1493; }
            h2 { color: #333; margin-top: 20px; }
            p { margin: 10px 0; }
            .contact-box { background: #f9f9f9; padding: 20px; border-radius: 8px; margin: 20px 0; }
        </style>
    </head>
    <body>
        <h1>Contact Us</h1>
        <p><strong>N&N Makeup Academy</strong></p>
        <p>We're here to help! Reach out to us through any of the following channels:</p>
        
        <div class="contact-box">
            <h2>📧 Email</h2>
            <p>support@nnmakeupandgrooming.com</p>
            <p>For general inquiries, course questions, and technical support</p>
        </div>
        
        <div class="contact-box">
            <h2>📱 Phone & WhatsApp</h2>
            <p>+91 9248444687</p>
            <p>Available: Monday to Saturday, 10:00 AM - 6:00 PM IST</p>
        </div>
        
        <div class="contact-box">
            <h2>🌐 Website</h2>
            <p><a href="https://www.nnmakeupandgrooming.com">www.nnmakeupandgrooming.com</a></p>
        </div>
        
        <div class="contact-box">
            <h2>📍 Address</h2>
            <p>N&N Makeup Academy</p>
            <p>Mittaighar, Hyderabad</p>
            <p>Telangana, India</p>
        </div>
        
        <h2>Business Hours</h2>
        <p><strong>Monday - Saturday:</strong> 10:00 AM - 6:00 PM IST</p>
        <p><strong>Sunday:</strong> Closed</p>
        
        <h2>Support Response Time</h2>
        <p>We typically respond to all inquiries within 24 hours during business days.</p>
        
        <h2>For Course-Related Queries</h2>
        <ul>
            <li>Course enrollment issues</li>
            <li>Payment problems</li>
            <li>Course access difficulties</li>
            <li>Certificate requests</li>
            <li>Refund inquiries</li>
        </ul>
        <p>Please contact us via email or WhatsApp with your order details.</p>
    </body>
    </html>
    """
