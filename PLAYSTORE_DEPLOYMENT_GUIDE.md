# 🚀 N&N Makeup Academy - Play Store Deployment Guide

## ✅ COMPLETED FEATURES

### Core Features Ready:
- ✅ Phone OTP Authentication (Twilio)
- ✅ 19 Courses (17 internal + 2 external TagMango)
- ✅ Course browsing with categories (Makeup, Nail, Hair)
- ✅ Detailed course pages with theory & practical videos
- ✅ Razorpay payment integration (UPI, Cards, Net Banking, Wallets)
- ✅ External course support (TagMango integration)
- ✅ Certificate system (auto-generated on completion)
- ✅ Admin panel for course management
- ✅ User profile with certificates display
- ✅ Video player for course lessons
- ✅ Progress tracking
- ✅ Price display in Indian Rupees (₹)

---

## 📋 DEPLOYMENT CHECKLIST

### Phase 1: App Configuration (30 mins)
- [ ] Update app.json with production settings
- [ ] Configure app icon (1024x1024px)
- [ ] Configure splash screen
- [ ] Set version number (1.0.0)
- [ ] Configure bundle identifier
- [ ] Set permissions

### Phase 2: Production Environment (15 mins)
- [ ] Update Razorpay to LIVE keys (currently TEST)
- [ ] Update Twilio to production credentials
- [ ] Configure production backend URL
- [ ] Test payment flow with real money (small amount)

### Phase 3: Build APK/AAB (30 mins)
- [ ] Install EAS CLI
- [ ] Configure EAS build
- [ ] Create production build (AAB format)
- [ ] Test APK on physical device

### Phase 4: Google Play Console (1-2 hours)
- [ ] Create Google Play Developer account ($25 one-time)
- [ ] Create new app listing
- [ ] Upload screenshots (phone & tablet)
- [ ] Write app description
- [ ] Set content rating
- [ ] Upload AAB file
- [ ] Submit for review

---

## 🎯 STEP-BY-STEP GUIDE

### **Step 1: Update app.json for Production**

Current app.json needs:
```json
{
  "expo": {
    "name": "N&N Makeup Academy",
    "slug": "nn-makeup-academy",
    "version": "1.0.0",
    "orientation": "portrait",
    "icon": "./assets/icon.png",
    "userInterfaceStyle": "light",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#FF1493"
    },
    "android": {
      "package": "com.nnacademy.makeupapp",
      "versionCode": 1,
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#FF1493"
      },
      "permissions": [
        "INTERNET",
        "ACCESS_NETWORK_STATE",
        "CAMERA",
        "READ_EXTERNAL_STORAGE",
        "WRITE_EXTERNAL_STORAGE"
      ]
    }
  }
}
```

### **Step 2: Create App Assets**

Required assets:
1. **App Icon** (1024x1024px)
   - Round icon with N&N branding
   - Pink (#FF1493) theme
   
2. **Splash Screen** (1242x2436px)
   - N&N logo centered
   - Pink background
   
3. **Screenshots** (minimum 2, max 8)
   - Phone: 1080x1920px or 1440x2560px
   - Show: Login, Course browsing, Course detail, Payment

### **Step 3: Production Keys**

Update `.env` files:

**Backend `.env`:**
```
RAZORPAY_KEY_ID=rzp_live_YOUR_LIVE_KEY
RAZORPAY_KEY_SECRET=your_live_secret_key
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_verified_number
```

**Frontend `.env`:**
```
EXPO_PUBLIC_BACKEND_URL=https://your-production-backend.com
```

### **Step 4: Build with EAS**

```bash
# Install EAS CLI
npm install -g eas-cli

# Login to Expo
eas login

# Configure build
eas build:configure

# Build for Android (Production)
eas build --platform android --profile production

# Download APK/AAB when ready
```

### **Step 5: Test Build**

Before submitting:
- [ ] Install APK on physical Android device
- [ ] Test login with real phone number
- [ ] Browse courses
- [ ] Test payment with ₹10 (smallest amount)
- [ ] Verify video playback
- [ ] Test certificate generation
- [ ] Check external course redirect

### **Step 6: Play Store Submission**

1. **Go to**: https://play.google.com/console
2. **Create App** → Select "N&N Makeup Academy"
3. **Complete Store Listing:**
   - Short description (80 chars max)
   - Full description (4000 chars max)
   - Screenshots (phone & tablet)
   - Feature graphic (1024x500px)
   - Category: Education
   - Content rating: Everyone
   
4. **Upload AAB** → Production → Release
5. **Submit for Review** (1-3 days)

---

## 📱 STORE LISTING TEXT

### Short Description (80 chars):
"Learn professional makeup, nails & hair styling from home. Expert courses!"

### Full Description:
```
N&N Makeup Academy - Your Gateway to Professional Beauty Education

🎓 LEARN FROM EXPERTS
Master professional makeup, nail art, and hair styling from certified instructor Irfana Begum. Our comprehensive courses are designed for aspiring makeup artists, salon owners, and beauty enthusiasts.

💄 WHAT YOU'LL LEARN
• Professional Makeup Mastery
• Bridal & Party Makeup
• Nail Care & Nail Art
• Hair Styling & Bridal Hair
• Beauty Business Management

✨ FEATURES
• 19+ Professional Courses
• Theory & Practical Video Lessons
• Earn Verified Certificates
• Learn at Your Own Pace
• Affordable Pricing (₹999 onwards)
• Secure Payment (UPI, Cards, Net Banking)

🎯 WHO IS THIS FOR?
• Aspiring Makeup Artists
• Salon & Beauty Parlor Owners
• Beauty Enthusiasts
• Career Switchers
• Home-Based Business Starters

📱 APP FEATURES
• Phone Number Login (OTP)
• Browse Courses by Category
• Video Lessons with Theory
• Track Your Progress
• Downloadable Certificates
• 24/7 Course Access

💰 FLEXIBLE PRICING
Courses starting from just ₹999! Professional certification programs also available.

🏆 WHY CHOOSE US?
• Expert Instructor with 10+ years experience
• Comprehensive Curriculum
• Hands-on Practical Training
• Industry-Recognized Certificates
• Lifetime Course Access
• Student Support

Download now and start your beauty career journey!

Contact: support@nnmakeupacademy.com
Website: www.nnmakeupandgrooming.com
```

---

## ⚠️ IMPORTANT NOTES

### Before Going Live:
1. **Test Payment**: Make a real ₹10 payment to verify Razorpay live mode
2. **Backup Database**: Export all courses data
3. **Terms & Privacy**: Ensure policy pages are accessible
4. **Customer Support**: Set up email/phone for user queries

### After Approval:
1. Monitor crash reports in Play Console
2. Respond to user reviews within 24 hours
3. Track download/install metrics
4. Plan v1.1 updates based on feedback

---

## 🎯 TIMELINE

**Total Time: 3-5 days**

- Day 1 (2-3 hours): Configure app.json, create assets, update keys
- Day 1 (1 hour): Build APK with EAS
- Day 1 (1 hour): Test on device
- Day 2 (2 hours): Create Play Store listing, upload screenshots
- Day 2 (30 mins): Submit for review
- Day 3-5: Google review process (1-3 days typically)

---

## ✅ READY TO START?

Would you like me to:
1. **Update app.json now** with production settings?
2. **Help create app assets** (icon, splash, screenshots)?
3. **Configure EAS build** for Play Store?
4. **Prepare store listing text**?

Let me know which step you'd like to start with!
