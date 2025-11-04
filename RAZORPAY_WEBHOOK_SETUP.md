# Razorpay Webhook & Manual Enrollment Setup

## ✅ What Has Been Added

### 1. Razorpay Webhook Handler
**Endpoint**: `POST /api/payment/razorpay-webhook`

This webhook automatically enrolls users when they complete payment on Razorpay.

**How it works**:
- Razorpay sends a webhook when payment is captured
- Backend verifies the payment
- User is automatically enrolled in the course
- No manual intervention needed

### 2. Manual Enrollment API (Admin Only)
**Endpoint**: `POST /api/admin/manual-enroll`

**Headers**:
```
Authorization: admin_[your-admin-token]
```

**Body**:
```json
{
  "user_phone": "8983690594",
  "course_id": "6901cbf1e7fae8cab852d3c2"
}
```

**Usage**: Allows admin to manually enroll any user in any course for testing.

---

## 🔧 How to Configure Razorpay Webhook

### Step 1: Login to Razorpay Dashboard
Visit: https://dashboard.razorpay.com/

### Step 2: Go to Settings → Webhooks
Navigate to: Settings → Webhooks → Create Webhook

### Step 3: Add Webhook URL
```
https://beauty-course-app.preview.emergentagent.com/api/payment/razorpay-webhook
```

### Step 4: Select Events
Check these events:
- ✅ payment.captured
- ✅ payment.failed (optional, for tracking)

### Step 5: Generate Webhook Secret
- Razorpay will generate a webhook secret
- Copy this secret
- Add it to your `.env` file:
```
RAZORPAY_WEBHOOK_SECRET=your_webhook_secret_here
```

### Step 6: Save & Activate
- Click "Create Webhook"
- Webhook is now active!

---

## 📱 Testing Manual Enrollment

### Using cURL:
```bash
curl -X POST https://beauty-course-app.preview.emergentagent.com/api/admin/manual-enroll \
  -H "Authorization: admin_your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "user_phone": "8983690594",
    "course_id": "6901cbf1e7fae8cab852d3c2"
  }'
```

### Using Admin Dashboard:
You can add a UI in the admin dashboard to manually enroll users for testing purposes.

---

## 🎯 Current Status

✅ **You are now enrolled** in the "Party & Evening Makeup Masterclass" course  
✅ **Go to "My Learning" tab** to see the course content  
✅ **Webhook handler is active** - future payments will auto-enroll  
✅ **Manual enrollment API is ready** for testing  

---

## 🚀 Next: Build APK with Android Studio

Ready to build the production APK? See `ANDROID_STUDIO_BUILD_GUIDE.md`
