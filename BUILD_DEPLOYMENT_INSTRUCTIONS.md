# 🚀 N&N Makeup Academy - Build & Deployment Instructions

## ✅ STEP 1: APP CONFIGURATION - COMPLETED!

Your app.json has been updated with:
- ✅ App Name: "N&N Makeup Academy"
- ✅ Package Name: com.nnacademy.makeupapp
- ✅ Version: 1.0.0
- ✅ Brand Color: #FF1493 (Pink)
- ✅ Permissions configured
- ✅ EAS configuration created

---

## 📱 STEP 2: BUILD PROCESS

### Option A: Build on Emergent Platform (Recommended)

**Important Note:** Since you're on Emergent platform, the typical EAS build process from your local machine may not work directly. You have **two options**:

#### **Option 1: Export Code & Build Locally** ✅
1. Download/Export your code from Emergent
2. On your local machine with Node.js installed:
   ```bash
   cd frontend
   npm install -g eas-cli
   npm install
   eas login
   eas build --platform android --profile production
   ```
3. Wait 15-30 mins for build to complete
4. Download the AAB file

#### **Option 2: Use Emergent's Deployment Feature** ✅
- Contact Emergent support to help with Play Store deployment
- They may have built-in deployment tools

---

## 🎨 STEP 3: CREATE APP ASSETS

You need to create these images:

### 1. App Icon (Required)
- **Size:** 1024x1024 pixels
- **Format:** PNG with no transparency
- **Content:** Your N&N logo/branding
- **Colors:** Use pink (#FF1493) theme
- **Save as:** `icon.png` in `assets/images/`

### 2. Adaptive Icon (Required for Android)
- **Size:** 1024x1024 pixels
- **Format:** PNG
- **Content:** Foreground layer of your icon
- **Save as:** `adaptive-icon.png` in `assets/images/`

### 3. Splash Screen (Required)
- **Size:** 1242x2436 pixels
- **Format:** PNG
- **Content:** N&N logo on pink background
- **Save as:** `splash-icon.png` in `assets/images/`

### 4. Screenshots (Required - minimum 2, max 8)
- **Size:** 1080x1920 pixels (portrait) or 1440x2560 pixels
- **Content:** Capture these screens from your app:
  1. Login screen with phone number
  2. Courses browse screen
  3. Course detail page
  4. Payment/Razorpay screen
  5. Profile with certificates
  6. Video player
  7. Admin panel (optional)
  8. Certificate view (optional)

**How to capture screenshots:**
- Open app in browser
- Use browser DevTools (F12) → Device Toolbar → Set to mobile size
- Take screenshots using snipping tool
- Or use your phone and take actual screenshots

### 5. Feature Graphic (Required)
- **Size:** 1024x500 pixels
- **Format:** PNG or JPG
- **Content:** Promotional banner with text like:
  "Learn Professional Makeup, Nails & Hair Styling from Home"
  "N&N Makeup Academy"

---

## 💳 STEP 4: PRODUCTION ENVIRONMENT SETUP

### Update Backend .env with LIVE Keys:

**Current (TEST MODE):**
```
RAZORPAY_KEY_ID=rzp_test_xxxxx
RAZORPAY_KEY_SECRET=test_secret
```

**Change to (LIVE MODE):**
```
RAZORPAY_KEY_ID=rzp_live_xxxxx
RAZORPAY_KEY_SECRET=live_secret
```

**To get Live Razorpay Keys:**
1. Login to https://dashboard.razorpay.com/
2. Go to Settings → API Keys
3. Generate LIVE mode keys
4. Activate your account (KYC required)
5. Update `.env` file

### Update Frontend .env (if needed):
```
EXPO_PUBLIC_BACKEND_URL=https://your-production-domain.com
```

---

## 🏪 STEP 5: GOOGLE PLAY CONSOLE SETUP

### 5.1 Create Developer Account
1. Go to: https://play.google.com/console
2. Sign in with Google account
3. Pay $25 registration fee (one-time)
4. Complete account setup

### 5.2 Create New App
1. Click "Create app"
2. Fill in:
   - **App name:** N&N Makeup Academy
   - **Default language:** English (India)
   - **App or game:** App
   - **Free or paid:** Free
   - **Declarations:** Accept all

### 5.3 Store Listing
Complete all sections:

**Main store listing:**
- **App name:** N&N Makeup Academy
- **Short description:**
  ```
  Learn professional makeup, nails & hair styling from home. Expert courses with certificates!
  ```
  
- **Full description:**
  ```
  🎓 N&N Makeup Academy - Professional Beauty Education

  Master makeup, nail art, and hair styling from certified instructor Irfana Begum. 
  
  ✨ FEATURES:
  • 19+ Professional Courses
  • Theory & Practical Videos
  • Earn Certificates
  • Affordable Pricing (₹999+)
  • Secure Payment (UPI/Cards)
  • Learn at Your Pace

  💄 COURSES:
  • Makeup Mastery
  • Bridal & Party Makeup
  • Nail Care & Art
  • Hair Styling
  • Beauty Business

  Perfect for aspiring makeup artists, salon owners, and beauty enthusiasts!

  📱 Download now and start your beauty career!
  ```

- **App icon:** Upload your 512x512 icon
- **Feature graphic:** Upload 1024x500 banner
- **Screenshots:** Upload 2-8 screenshots
- **Category:** Education
- **Tags:** makeup, beauty, education, courses
- **Contact details:**
  - Email: irfanabegum@nnmakeupacademy.com
  - Phone: +91-XXXXXXXXXX (your contact)
  - Website: https://nnmakeupandgrooming.com

### 5.4 Content Rating
1. Start questionnaire
2. Select: Education
3. Answer questions (all "No" for your app type)
4. Apply rating

### 5.5 App Content
Complete:
- **Privacy Policy:** Required! Must have URL
  Example: https://your-website.com/privacy-policy
  (You can use the policy content from your backend `/api/policies/privacy`)
  
- **App access:** All features available to all users
- **Ads:** No (you don't have ads)
- **Target audience:** 18 and older
- **News app:** No

### 5.6 Upload AAB/APK
1. Go to: Production → Releases
2. Click "Create new release"
3. Upload your AAB file (from EAS build)
4. Add release notes:
   ```
   Initial release v1.0.0
   - Professional makeup, nail, hair courses
   - Phone OTP authentication
   - Razorpay payment integration
   - Certificate generation
   - 19+ courses available
   ```
5. Save and review

### 5.7 Submit for Review
1. Review all sections (must be complete)
2. Click "Start rollout to Production"
3. Wait 1-3 days for Google review

---

## ⏱️ TIMELINE

**Total: 2-4 days**

| Task | Time | Your Progress |
|------|------|---------------|
| ✅ App configuration | 30 mins | DONE |
| Create assets (icon, screenshots) | 1-2 hours | TODO |
| Setup Google Dev account | 30 mins | TODO |
| Complete store listing | 1 hour | TODO |
| Build APK with EAS | 30 mins | TODO |
| Upload & submit | 30 mins | TODO |
| Google review | 1-3 days | WAITING |

---

## 📋 CHECKLIST

### Before Building:
- [ ] App icon created (1024x1024)
- [ ] Splash screen created
- [ ] Screenshots captured (minimum 2)
- [ ] Feature graphic created (1024x500)
- [ ] Razorpay LIVE keys obtained
- [ ] Privacy policy URL ready

### Before Submitting:
- [ ] Google Developer account created ($25 paid)
- [ ] Store listing completed
- [ ] Content rating done
- [ ] AAB/APK file ready
- [ ] All sections reviewed

### After Approval:
- [ ] App published on Play Store
- [ ] Monitor reviews and ratings
- [ ] Respond to user feedback
- [ ] Track downloads in console

---

## 🆘 NEED HELP?

### Common Issues:

**Q: I can't build with EAS on Emergent?**
A: Export your code and build locally, OR contact Emergent support for deployment help.

**Q: Don't have graphic design skills for assets?**
A: Use free tools:
- Canva.com (easy icon/graphic maker)
- Figma.com (professional design tool)
- Or hire a designer on Fiverr ($5-20)

**Q: Razorpay not accepting my documents?**
A: Ensure:
- Business PAN card
- GST certificate (if applicable)  
- Bank account details
- Business address proof

**Q: Google rejected my app?**
A: Common reasons:
- Missing privacy policy
- Incomplete store listing
- Icon/screenshots quality
- Check rejection reason and fix

---

## 🎯 NEXT STEPS FOR YOU:

1. **Create app assets** (icon, screenshots) - 1-2 hours
2. **Get Razorpay LIVE keys** - 30 mins
3. **Create Google Developer account** - 30 mins
4. **Export code from Emergent** OR **contact Emergent for build help**
5. **Follow store listing steps** above
6. **Submit for review**

**Your app is ready! Just need the assets and accounts setup.** 🚀

Let me know if you need help with any specific step!
