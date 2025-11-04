# 🚀 N&N Makeup Academy - Build Instructions for Your Computer

## ✅ EVERYTHING IS READY!

You have:
- ✅ Code in GitHub: https://github.com/mittalgharirfana/nn-makeup-academy
- ✅ Screenshots ready
- ✅ LIVE Razorpay keys configured
- ✅ All guides created

---

## 🏗️ BUILD APK ON YOUR COMPUTER (30 minutes)

### **Step 1: Clone Your Code**

Open terminal/command prompt and run:

```bash
git clone https://github.com/mittalgharirfana/nn-makeup-academy.git
cd nn-makeup-academy/frontend
```

### **Step 2: Install Dependencies**

```bash
npm install
```

If errors occur, try:
```bash
npm install --legacy-peer-deps
```

### **Step 3: Install EAS CLI**

```bash
npm install -g eas-cli
```

### **Step 4: Login to Expo**

```bash
eas login
```

When prompted:
- **Username:** mittaigharirfana786
- **Password:** Mittaighar@1982

### **Step 5: Configure Build (First Time Only)**

```bash
eas build:configure
```

Select:
- Platform: **Android**
- Build type: **app-bundle** (for Play Store)

### **Step 6: Build for Play Store**

```bash
eas build --platform android --profile production
```

This will:
- Upload your code to Expo servers
- Build in cloud (takes 20-30 minutes)
- Give you download link when done

### **Step 7: Download AAB File**

When build completes:
- You'll get a download link in terminal
- Or check: https://expo.dev/accounts/mittaigharirfana786/projects/nn-makeup-academy/builds
- Download the **.aab** file

---

## 🏪 SUBMIT TO GOOGLE PLAY STORE (30 minutes)

### **Step 1: Go to Play Console**

1. Visit: https://play.google.com/console
2. Sign in with your Google account
3. Click **"Create app"**

### **Step 2: App Details**

Fill in:
- **App name:** N&N Makeup Academy
- **Default language:** English (India)
- **App or game:** App
- **Free or paid:** Free

Check all declarations → Click **Create app**

### **Step 3: Store Listing**

Go to "Store listing" (left sidebar):

**Short description (80 chars):**
```
Learn makeup, nails & hair styling. Expert courses with certificates!
```

**Full description:**
```
🎓 N&N Makeup Academy - Professional Beauty Education

Master makeup, nail art, and hair styling from certified instructor Irfana Begum.

✨ FEATURES:
• 19+ Professional Courses
• Video Lessons with Theory
• Earn Certificates on Completion
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

📱 APP FEATURES:
• Phone OTP Login
• Browse Courses by Category
• Track Your Progress
• Downloadable Certificates
• 24/7 Course Access

💰 FLEXIBLE PRICING:
Courses starting from just ₹999!

Perfect for aspiring makeup artists and beauty enthusiasts!

📱 Download now and start your beauty career!

Contact: irfanabegum@nnmakeupacademy.com
Website: https://nnmakeupandgrooming.com
```

**App icon:** Your icon file (512x512 minimum)

**Screenshots:** Upload the 2 screenshots we captured

**Category:** Education

**Contact details:**
- Email: irfanabegum@nnmakeupacademy.com
- Phone: Your phone number
- Website: https://nnmakeupandgrooming.com

Click **Save**

### **Step 4: Content Rating**

1. Click "Content rating" (left sidebar)
2. Click "Start questionnaire"
3. **Category:** Education
4. Answer questions (mostly select "No")
5. Click **Submit**
6. Click **Apply rating**

### **Step 5: Target Audience**

1. Click "Target audience"
2. **Age:** 18 and older
3. Click **Save**

### **Step 6: Data Safety**

1. Click "Data safety"
2. **Collects personal info:** Yes (Name, Phone number)
3. **Collects financial info:** Yes (Payment info)
4. **Data encrypted:** Yes
5. **Privacy policy URL:** https://nnmakeupandgrooming.com/privacy
6. Click **Save**

### **Step 7: App Content**

Complete all sections:
- **Ads:** No
- **In-app purchases:** No (payment is for course access)
- **Content guidelines:** Accept

### **Step 8: Production Release**

1. Go to **Production** (left sidebar)
2. Click **Countries/regions**
3. Select **India** (+ any other countries)
4. Click **Save**

### **Step 9: Create Release**

1. Click **Create new release**
2. Upload your **.aab** file
3. **Release name:** 1.0.0
4. **Release notes:**
```
Initial release of N&N Makeup Academy

• Professional makeup, nail art, and hair styling courses
• 19+ courses available
• Secure payment with Razorpay (UPI, Cards, Net Banking)
• Phone OTP authentication
• Certificate generation on course completion
• Video lessons with theory content
```
5. Click **Save**
6. Click **Review release**

### **Step 10: Submit for Review**

1. Check all sections are ✅ complete
2. Click **"Start rollout to Production"**
3. Confirm

**🎉 DONE! Wait 1-3 days for Google review**

---

## ⏱️ TIMELINE

**Today:**
- Clone code: 5 mins
- Install dependencies: 10 mins
- Build APK: 30 mins
- Fill Play Store form: 30 mins
- Submit: 5 mins
**Total: ~1.5 hours**

**Google Review:** 1-3 days

---

## ⚠️ IMPORTANT NOTES

### **Razorpay Keys**
Your LIVE keys are in the code:
- Key ID: rzp_live_RbKBTYfMg8MDci
- Secret: 5hF6YB26hB4kT7W8sr9mxJtO

**⚠️ SECURITY:** After deployment, regenerate these keys in Razorpay dashboard!

### **Testing Before Going Live**
1. Download APK on your phone
2. Test with ₹10 payment
3. Verify money reaches your account
4. Then make app public

### **After Approval**
- App goes live on Play Store
- Students can download and pay
- Monitor Razorpay dashboard for transactions
- Respond to user reviews

---

## 🆘 IF YOU FACE ISSUES

### **Build Fails**
```bash
cd frontend
rm -rf node_modules
npm install --legacy-peer-deps
eas build --platform android --profile production
```

### **Dependencies Error**
```bash
npm install expo@latest
npm install --force
```

### **EAS Login Issues**
- Make sure you're using: mittaigharirfana786
- Password: Mittaighar@1982
- If issues, reset password at: https://expo.dev

### **Play Store Rejection**
Common reasons:
- Missing privacy policy
- Incomplete content rating
- Screenshot quality
- Check rejection email and fix

---

## ✅ YOUR CHECKLIST

**Before Building:**
- [ ] Node.js installed
- [ ] Git installed
- [ ] Code cloned from GitHub
- [ ] npm install completed
- [ ] EAS CLI installed

**Before Submitting:**
- [ ] AAB file downloaded
- [ ] Screenshots ready
- [ ] App icon ready
- [ ] Privacy policy URL ready
- [ ] Google Developer account ready

**After Submitting:**
- [ ] All Play Console sections complete
- [ ] Release submitted
- [ ] Monitoring email for Google response

---

## 🎯 YOU HAVE EVERYTHING!

✅ Code in GitHub  
✅ Screenshots  
✅ LIVE Razorpay  
✅ Complete guides  
✅ Ready to build!

**Total time needed: 1.5 hours at home + 1-3 days Google review**

**Good luck with your Play Store launch! 🚀**
