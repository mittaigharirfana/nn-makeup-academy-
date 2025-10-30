# 🏠 N&N Makeup Academy - Setup on Your Computer Guide

## ✅ WHAT YOU NEED TO DO NOW (Before Leaving)

---

## 📦 STEP 1: PUSH CODE TO GITHUB (Do this now - 5 mins)

1. **In Emergent Platform:**
   - Click your **profile icon** (top right)
   - Click "**Connect GitHub**"
   - Grant permissions to your GitHub account

2. **Save Your Code:**
   - Look for "**Save to GitHub**" button (in chat or toolbar)
   - Select "**Create new repository**" 
   - Name it: `nn-makeup-academy`
   - Click "**PUSH TO GITHUB**"
   - Wait for confirmation

3. **Verify:**
   - Go to https://github.com/YOUR_USERNAME
   - You should see `nn-makeup-academy` repository
   - ✅ Your code is now backed up!

---

## 💻 STEP 2: SETUP ON YOUR COMPUTER (At home)

### **What You Need to Install:**

#### **A. Node.js (Required)**
1. Download: https://nodejs.org/
2. Choose: LTS version (20.x or higher)
3. Install with default settings
4. Verify: Open terminal/command prompt
   ```bash
   node --version
   npm --version
   ```

#### **B. Git (Required)**
1. Download: https://git-scm.com/downloads
2. Install with default settings
3. Verify:
   ```bash
   git --version
   ```

#### **C. EAS CLI (Required for building)**
```bash
npm install -g eas-cli
```

#### **D. Expo CLI (Optional but helpful)**
```bash
npm install -g @expo/cli
```

---

## 🚀 STEP 3: CLONE & SETUP PROJECT

### **On Your Computer:**

```bash
# 1. Clone your repository
git clone https://github.com/YOUR_USERNAME/nn-makeup-academy.git
cd nn-makeup-academy

# 2. Setup Frontend
cd frontend
npm install

# 3. Setup Backend (if you want to run locally)
cd ../backend
pip install -r requirements.txt

# 4. You're ready!
```

---

## 🏗️ STEP 4: BUILD FOR PLAY STORE

### **When Ready to Build:**

```bash
cd frontend

# Login to Expo (create free account if needed)
eas login

# Build for Play Store
eas build --platform android --profile production
```

**This will:**
- Build in Expo cloud (not on your computer)
- Take 20-30 minutes
- Give you download link for AAB file
- No Android Studio needed!

---

## 📸 STEP 5: SCREENSHOTS

### **Take screenshots before leaving OR at home:**

**Option A: From Running App**
```bash
cd frontend
npx expo start
```
- Open in browser
- Press F12 → Mobile view
- Take screenshots

**Option B: From Live URL**
- Open: https://makeupacademy.preview.emergentagent.com
- Take screenshots now
- Save on your computer

**Need 4 screenshots:**
1. Login screen
2. Courses browse
3. Course detail
4. Payment screen

---

## 📋 DOCUMENTS TO TAKE WITH YOU

I've created these guides for you (they're in `/app/` folder):

1. **BUILD_DEPLOYMENT_INSTRUCTIONS.md** - Complete deployment guide
2. **PLAYSTORE_DEPLOYMENT_GUIDE.md** - Play Store details
3. **BUILD_NOW_GUIDE.md** - Quick reference

**How to access them:**
- They'll be in your GitHub repository
- Or save them to your computer now

---

## 🏪 PLAY STORE SUBMISSION (At Home)

### **What You'll Do:**

1. **Build APK** (30 mins)
   ```bash
   eas build --platform android --profile production
   ```

2. **Go to Play Console** (30 mins)
   - https://play.google.com/console
   - Fill store listing
   - Upload screenshots
   - Upload AAB file

3. **Submit** (5 mins)
   - Review everything
   - Click "Start rollout"

4. **Wait** (1-3 days)
   - Google reviews your app
   - You get email: Approved or changes needed

---

## ✅ CHECKLIST BEFORE YOU LEAVE

### **Must Do Now:**
- [ ] Connect GitHub in Emergent
- [ ] Push code to GitHub
- [ ] Verify repository exists on GitHub.com
- [ ] Take 4 screenshots (or note the live URL)
- [ ] Save app icon (if you have separate file)

### **Do At Home:**
- [ ] Install Node.js
- [ ] Install Git
- [ ] Clone repository
- [ ] Install dependencies (`npm install`)
- [ ] Install EAS CLI
- [ ] Build APK
- [ ] Submit to Play Store

---

## 📱 YOUR APP INFO

**Save this for reference:**

**App Details:**
- Name: N&N Makeup Academy
- Package: com.nnacademy.makeupapp
- Version: 1.0.0

**GitHub:**
- Repository: YOUR_USERNAME/nn-makeup-academy

**Play Store:**
- Console: https://play.google.com/console
- Email: irfanabegum@nnmakeupacademy.com

**Razorpay:**
- Dashboard: https://dashboard.razorpay.com
- Status: KYC submitted (waiting for approval)

---

## 🆘 HELP AT HOME

### **If Build Fails:**
```bash
# Clear cache and retry
cd frontend
rm -rf node_modules
npm install
eas build --platform android --profile production
```

### **If Dependencies Error:**
```bash
# Update Expo
npm install expo@latest

# Fix peer dependencies
npm install --legacy-peer-deps
```

### **Need Help?**
- Expo docs: https://docs.expo.dev/build/setup/
- Play Store help: https://support.google.com/googleplay/android-developer

---

## ⏱️ TIMELINE (At Home)

**Day 1 (1-2 hours):**
- Install Node.js, Git
- Clone repository
- Build APK with EAS

**Day 2 (1 hour):**
- Fill Play Console form
- Upload screenshots
- Submit for review

**Day 3-5:**
- Wait for Google approval
- Check email daily

---

## 🎯 WHAT TO DO NOW

**Before You Leave (10 mins):**
1. ✅ Push code to GitHub
2. ✅ Take screenshots (or save URL)
3. ✅ Download this guide
4. ✅ Note down your GitHub repo name

**At Home (2-3 hours):**
1. Install software (Node.js, Git)
2. Clone repository
3. Build APK
4. Submit to Play Store

---

## 💡 PRO TIPS

**For Faster Setup:**
- Download Node.js installer before leaving (save offline)
- Take screenshots now (save time at home)
- Write down your GitHub username/password
- Take photo of QR code if you want to test on phone

**For Smooth Build:**
- Ensure good internet connection (build is cloud-based)
- Have Expo account credentials ready
- Keep Play Console login details handy

---

**Your app is ready! Just need to:**
1. Push to GitHub (now)
2. Setup on your computer (at home)
3. Build & submit (2-3 hours)

**Good luck! 🚀**
