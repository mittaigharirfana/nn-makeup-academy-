# 🏠 N&N Makeup Academy - Complete Home Deployment Guide

## 📋 PREREQUISITES

Before starting, install these on your computer:

### 1. Install Node.js (Required)
- **Download:** https://nodejs.org/
- **Version:** LTS (Long Term Support) - v20 or higher
- **Install:** Run installer with default settings
- **Verify:**
  ```bash
  node --version
  npm --version
  ```
  You should see version numbers (e.g., v20.x.x)

### 2. Install Git (Required)
- **Download:** https://git-scm.com/downloads
- **Install:** Run installer with default settings
- **Verify:**
  ```bash
  git --version
  ```
  You should see version number (e.g., git version 2.x.x)

---

## 🚀 STEP-BY-STEP DEPLOYMENT

### ✅ STEP 1: CLONE CODE FROM GITHUB (5 mins)

Open Terminal (Mac) or Command Prompt (Windows):

```bash
# Navigate to where you want to save the project
cd Desktop

# Clone your repository
git clone https://github.com/mittalgharirfana/nn-makeup-academy.git

# Enter the project folder
cd nn-makeup-academy

# Verify you have the code
ls
```

You should see folders: `frontend`, `backend`, and various `.md` files.

---

### ✅ STEP 2: CREATE .ENV FILE WITH NEW KEYS (2 mins)

#### For Windows:
```bash
# Navigate to backend folder
cd backend

# Create .env file
notepad .env
```

#### For Mac/Linux:
```bash
# Navigate to backend folder
cd backend

# Create .env file
nano .env
```

**Copy and paste this into the .env file:**

```env
MONGO_URL="mongodb://localhost:27017"
DB_NAME="nnacademy_database"
RAZORPAY_KEY_ID=rzp_live_RbYT5VTrqOUcNx
RAZORPAY_KEY_SECRET=qZgz2oXMEaZxY2G0jQtIbawB
TWILIO_ACCOUNT_SID=AC44f43f2a2d4cb5e8eaec8307ed29588b
TWILIO_AUTH_TOKEN=10623a066b0fc323b079fd7f7faa96ba
TWILIO_PHONE_NUMBER=+16602286999
ADMIN_USERNAME=admin@nnacademy.com
ADMIN_PASSWORD=Admin@123
```

**Save the file:**
- Windows (Notepad): File → Save → Close
- Mac/Linux (nano): Press `Ctrl+X` → Press `Y` → Press `Enter`

**Verify .env was created:**
```bash
# Check if file exists
ls .env
```

---

### ✅ STEP 3: INSTALL DEPENDENCIES (10 mins)

#### 3A. Install Frontend Dependencies

```bash
# Go back to main folder
cd ..

# Navigate to frontend folder
cd frontend

# Install all packages
npm install
```

**If you get errors**, try:
```bash
npm install --legacy-peer-deps
```

Wait for installation to complete (takes 5-10 minutes).

#### 3B. Install EAS CLI Globally

```bash
npm install -g eas-cli
```

**Verify EAS is installed:**
```bash
eas --version
```

You should see version number (e.g., eas-cli/x.x.x)

---

### ✅ STEP 4: BUILD APK WITH EAS (30 mins)

#### 4A. Login to Expo

```bash
eas login
```

**Enter your credentials:**
- **Username:** mittaigharirfana786
- **Password:** Mittaighar@1982

Press Enter after each.

**You should see:** "Logged in as mittaigharirfana786"

#### 4B. Configure Build (First Time Only)

```bash
eas build:configure
```

**When prompted:**
- "Generate a new Android Keystore?" → Press `Y` (Yes)
- "Generate a new Apple certificate?" → Press `N` (No, we're only doing Android)

#### 4C. Start the Build

```bash
eas build --platform android --profile production
```

**What happens:**
1. EAS uploads your code to Expo servers
2. Build starts in the cloud (you'll see a link)
3. Progress shows in terminal
4. Takes 20-30 minutes

**You'll see output like:**
```
✔ Build queued
✔ Build in progress...
○ Build URL: https://expo.dev/...
```

**WAIT** for the build to complete. You can:
- Watch progress in terminal
- Or visit the Build URL in browser

#### 4D. Download AAB File

When build completes:
```
✔ Build finished!
Download URL: https://expo.dev/.../application.aab
```

**Two ways to download:**

**Option 1: From Terminal**
```bash
eas build:download --id YOUR_BUILD_ID
```

**Option 2: From Browser**
- Click the download link
- Save the `.aab` file to Desktop
- File name will be like: `application-xxxxx.aab`

---

### ✅ STEP 5: SUBMIT TO PLAY STORE (30 mins)

#### 5A. Go to Play Console

1. Open browser: https://play.google.com/console
2. Sign in with your Google account
3. Click **"Create app"**

#### 5B. Basic App Information

Fill in:
- **App name:** N&N Makeup Academy
- **Default language:** English (India)
- **App or game:** App
- **Free or paid:** Free
- Check all policy boxes
- Click **"Create app"**

#### 5C. Store Listing (Left Sidebar)

Click "Store listing" and fill:

**App name:**
```
N&N Makeup Academy
```

**Short description (80 characters max):**
```
Learn makeup, nails & hair styling. Expert courses with certificates!
```

**Full description:**
```
🎓 N&N Makeup Academy - Professional Beauty Education

Master makeup, nail art, and hair styling from certified instructor Irfana Begum. Learn from home at your own pace!

✨ FEATURES:
• 19+ Professional Courses
• Video Lessons with Theory
• Earn Verified Certificates
• Affordable Pricing (₹999+)
• Secure Payment (UPI, Cards, Net Banking)
• Learn at Your Own Pace

💄 COURSE CATEGORIES:
• Professional Makeup Mastery
• Bridal & Party Makeup
• Nail Care & Nail Art
• Hair Styling & Bridal Hair
• Beauty Business Management

🎯 PERFECT FOR:
• Aspiring Makeup Artists
• Salon & Beauty Parlor Owners
• Beauty Enthusiasts
• Career Switchers
• Home-Based Business Starters

📱 APP FEATURES:
• Phone OTP Login
• Browse Courses by Category
• Video Lessons
• Track Your Progress
• Downloadable Certificates
• 24/7 Course Access

💰 FLEXIBLE PRICING:
Courses starting from just ₹999! Professional certification programs also available.

Perfect for aspiring makeup artists and beauty enthusiasts!

Download now and start your beauty career journey!

Contact: irfanabegum@nnmakeupacademy.com
Website: https://nnmakeupandgrooming.com
```

**App icon:**
- Click "Upload" → Select your icon file (512x512 minimum)

**Feature graphic:**
- Upload 1024x500 banner (create on Canva if needed)

**Phone screenshots:**
- Upload the 2 screenshots we captured
- Add more if you have them

**App category:** Education

**Tags:** makeup, beauty, education, courses, learning

**Contact details:**
- **Email:** irfanabegum@nnmakeupacademy.com
- **Phone:** Your phone number
- **Website:** https://nnmakeupandgrooming.com

Click **Save**

#### 5D. Content Rating (Left Sidebar)

1. Click "Content rating"
2. Click **"Start questionnaire"**
3. **Email:** Your email
4. **Category:** Education
5. Answer all questions (select "No" for most)
   - Violence? No
   - Sexual content? No
   - Language? No
   - Controlled substances? No
   - Interactive elements? No
6. Click **"Submit"**
7. Click **"Apply rating"**

#### 5E. Target Audience (Left Sidebar)

1. Click "Target audience"
2. **Target age group:** 18 and older
3. Click **"Next"**
4. Click **"Save"**

#### 5F. Data Safety (Left Sidebar)

1. Click "Data safety"
2. Click **"Start"**

**Data collection:**
- Does your app collect user data? **Yes**
- Select:
  - **Personal info:** Name, Phone number
  - **Financial info:** Payment info

**Data sharing:**
- Do you share data with third parties? **No**

**Data security:**
- Is data encrypted in transit? **Yes**
- Can users request data deletion? **Yes**

**Privacy policy:**
- Enter: `https://nnmakeupandgrooming.com/privacy`

Click **"Save"**

#### 5G. App Content (Complete All)

**Ads:**
- Does your app contain ads? **No**
- Click **Save**

**In-app purchases:**
- Skip (payment is for course access)

**Content guidelines:**
- Accept all
- Click **Save**

#### 5H. Store Settings (Left Sidebar)

1. Click "Store settings"
2. **App category:** Education → Other
3. Click **"Save"**

#### 5I. Production (Left Sidebar)

1. Click **"Production"**
2. Click **"Countries/regions"**
3. Select **India** (+ any other countries you want)
4. Click **"Save"**

#### 5J. Create Release

1. Click **"Create new release"**
2. Click **"Upload"** in App bundles section
3. Select your `.aab` file (downloaded from EAS)
4. Wait for upload (takes 2-5 minutes)

**Release name:**
```
1.0.0
```

**Release notes:**
```
Initial release of N&N Makeup Academy

Features:
• Professional makeup, nail art, and hair styling courses
• 19+ courses with theory and practical lessons
• Secure payment with Razorpay (UPI, Cards, Net Banking)
• Phone OTP authentication
• Certificate generation on course completion
• Video lessons and progress tracking
```

5. Click **"Save"**
6. Click **"Review release"**

#### 5K. Final Submit

1. Review all sections - ensure all are ✅ complete
2. If any section is ❌ red, go fix it
3. When all complete, click **"Start rollout to Production"**
4. Click **"Rollout"** to confirm

**🎉 SUBMITTED!**

---

## ⏱️ WHAT HAPPENS NEXT

### Google Review Process (1-3 days)

**Timeline:**
- **Day 1-2:** Google tests your app
- **Day 2-3:** You receive email

**Possible outcomes:**

**1. APPROVED ✅**
- Your app goes LIVE automatically
- Available on Play Store
- Students can download and enroll

**2. CHANGES NEEDED ⚠️**
- Google sends email with issues
- Fix the issues mentioned
- Resubmit (usually approved quickly)

Common issues:
- Missing privacy policy
- Incomplete content rating
- Screenshot quality
- Icon size issues

---

## 🧪 TESTING BEFORE GOING PUBLIC

### Test with Real Payment

**Before making app fully public:**

1. Download APK on your Android phone
2. Install and open app
3. Login with your phone number
4. Browse courses
5. Enroll in cheapest course (₹999)
6. Complete payment with real money
7. Verify:
   - Payment succeeds
   - Money appears in Razorpay dashboard
   - Course access granted
   - You can view videos

**If test successful** ✅ App is ready for users!

---

## 📊 AFTER APP GOES LIVE

### Monitor Your App

**Razorpay Dashboard:**
- Check: https://dashboard.razorpay.com
- View transactions
- Track revenue
- Monitor payment issues

**Play Console:**
- Check: https://play.google.com/console
- View download numbers
- Read user reviews
- Respond to feedback

**Respond to Reviews:**
- Reply within 24 hours
- Be professional and helpful
- Address issues quickly

---

## 🆘 TROUBLESHOOTING

### Build Issues

**Error: "Cannot find module"**
```bash
cd frontend
rm -rf node_modules
npm install --legacy-peer-deps
eas build --platform android --profile production
```

**Error: "No such file or directory"**
- Make sure you're in `frontend` folder
- Run: `pwd` to check current folder

**Build fails with "Invalid keystore"**
```bash
eas build --platform android --profile production --clear-cache
```

### Play Store Issues

**"Privacy policy not accessible"**
- Ensure https://nnmakeupandgrooming.com/privacy is working
- Test by opening in browser

**"Screenshots don't meet requirements"**
- Minimum size: 320px
- Recommended: 1080x1920px
- Format: PNG or JPG

**"App crashes on testing"**
- Check backend is running
- Verify Razorpay keys are correct
- Test on physical device first

---

## ✅ QUICK CHECKLIST

### Before Building:
- [ ] Node.js installed
- [ ] Git installed
- [ ] Code cloned from GitHub
- [ ] .env file created with new keys
- [ ] Dependencies installed (npm install)
- [ ] EAS CLI installed

### During Build:
- [ ] Logged in to Expo
- [ ] Build started successfully
- [ ] Waited for build completion (20-30 mins)
- [ ] AAB file downloaded

### Before Submitting:
- [ ] Google Developer account ready
- [ ] App icon prepared (512x512)
- [ ] Screenshots ready (minimum 2)
- [ ] Store descriptions written
- [ ] Privacy policy URL working

### During Submission:
- [ ] App created in Play Console
- [ ] Store listing filled
- [ ] Content rating completed
- [ ] Target audience set
- [ ] Data safety completed
- [ ] AAB file uploaded
- [ ] Release notes written
- [ ] All sections ✅ complete

### After Submission:
- [ ] Confirmation email received
- [ ] Monitoring email for Google response
- [ ] Ready to fix issues if any
- [ ] Prepared to test with real payment

---

## 💡 PRO TIPS

### For Faster Process:

1. **Prepare while building:**
   - While EAS builds (20-30 mins), start filling Play Console form
   - Write descriptions
   - Prepare screenshots

2. **Keep these handy:**
   - Razorpay keys (write in notepad)
   - Expo credentials
   - GitHub URL
   - Contact email

3. **Test thoroughly:**
   - Don't rush to make public
   - Test with ₹10 first
   - Verify everything works

### Common Mistakes to Avoid:

❌ Forgetting to create .env file
❌ Using old Razorpay keys
❌ Not waiting for build to complete
❌ Skipping content rating
❌ Uploading APK instead of AAB
❌ Making app public without testing

---

## 📞 GET HELP

**Build Issues:**
- Expo docs: https://docs.expo.dev/build/setup/
- Search error on Google
- Check Expo forums

**Play Store Issues:**
- Google support: https://support.google.com/googleplay/android-developer
- Read rejection email carefully
- Fix exactly what they ask

**Payment Issues:**
- Razorpay support: support@razorpay.com
- Check Razorpay dashboard for transaction status

---

## 🎯 SUMMARY

**Total Time:** ~1.5 hours + 1-3 days Google review

**Steps:**
1. Clone code (5 mins)
2. Create .env (2 mins)
3. Install dependencies (10 mins)
4. Build APK (30 mins)
5. Submit to Play Store (30 mins)
6. Wait for approval (1-3 days)
7. Test with real payment (15 mins)
8. Go live! 🎉

**You have everything you need!**

---

**🚀 Good luck with your Play Store deployment!**
**📱 Your N&N Makeup Academy app will be live soon!**
**💪 You've got this!**
