# Railway.app Deployment Guide - N&N Makeup Academy Backend

## Step-by-Step Deployment Instructions

### Prerequisites
- GitHub account (free)
- Railway account (free to start, ~$5/month after trial)
- MongoDB Atlas account (free tier available)

---

## Part 1: Setup MongoDB Atlas (Free Database)

### Step 1: Create MongoDB Atlas Account
1. Go to https://www.mongodb.com/cloud/atlas/register
2. Sign up with Google or email
3. Choose **FREE** M0 tier
4. Select a cloud provider and region (closest to you)
5. Create cluster (takes 1-3 minutes)

### Step 2: Get MongoDB Connection String
1. Click **"Connect"** on your cluster
2. Choose **"Connect your application"**
3. Copy the connection string (looks like):
   ```
   mongodb+srv://username:<password>@cluster0.xxxxx.mongodb.net/
   ```
4. Replace `<password>` with your actual password
5. Add database name at the end:
   ```
   mongodb+srv://username:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/makeup_academy
   ```
6. **Save this string** - you'll need it for Railway

### Step 3: Whitelist All IPs
1. In Atlas, go to **Network Access**
2. Click **"Add IP Address"**
3. Click **"Allow Access from Anywhere"** (0.0.0.0/0)
4. Click **"Confirm"**

---

## Part 2: Push Code to GitHub

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `nn-makeup-academy`
3. Make it **Private**
4. Click **"Create repository"**

### Step 2: Push Your Code
On your computer, open Command Prompt in your project folder:

```bash
cd C:\Users\ABDUL NAVEEN ANSARI\nn-makeup-academy
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/nn-makeup-academy.git
git push -u origin main
```

(Replace `YOUR_USERNAME` with your GitHub username)

---

## Part 3: Deploy to Railway

### Step 1: Create Railway Account
1. Go to https://railway.app
2. Click **"Login"**
3. Sign in with GitHub
4. Authorize Railway

### Step 2: Create New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose your **nn-makeup-academy** repository
4. Railway will auto-detect and deploy

### Step 3: Configure Environment Variables
1. Go to your project dashboard
2. Click on your service
3. Go to **"Variables"** tab
4. Add these environment variables ONE BY ONE:

```
MONGO_URL=mongodb+srv://YOUR_MONGODB_CONNECTION_STRING
DB_NAME=makeup_academy
ADMIN_USERNAME=admin@nnacademy.com
ADMIN_PASSWORD=Admin@123
ADMIN_TOKEN=your-secure-admin-token-here
RAZORPAY_KEY_ID=YOUR_RAZORPAY_KEY_ID
RAZORPAY_KEY_SECRET=YOUR_RAZORPAY_KEY_SECRET
TWILIO_ACCOUNT_SID=YOUR_TWILIO_SID
TWILIO_AUTH_TOKEN=YOUR_TWILIO_AUTH_TOKEN
TWILIO_PHONE_NUMBER=YOUR_TWILIO_PHONE
```

### Step 4: Get Your Backend URL
1. Go to **"Settings"** tab
2. Under **"Domains"**, you'll see your Railway URL
3. It will look like: `https://nn-makeup-academy-production.up.railway.app`
4. **Copy this URL** - this is your backend URL!

### Step 5: Test Your Backend
Open this URL in your browser:
```
https://YOUR-RAILWAY-URL.railway.app/api/courses
```

You should see your courses list (or empty array if no courses yet).

---

## Part 4: Update Mobile App

### Step 1: Update app.json
In your `frontend/app.json`, update the `extra` section:

```json
"extra": {
  "backendUrl": "https://YOUR-RAILWAY-URL.railway.app"
}
```

Replace `YOUR-RAILWAY-URL` with your actual Railway URL.

### Step 2: Rebuild APK/AAB
```bash
cd C:\Users\ABDUL NAVEEN ANSARI\nn-makeup-academy\frontend
eas build --platform android --profile production
```

### Step 3: Download and Test
1. Download the new APK/AAB
2. Install on your phone
3. Test all features - they should now work!

---

## Troubleshooting

### Issue: "Application Error" on Railway URL
**Solution:** Check the deployment logs in Railway. Common issues:
- Missing environment variables
- Wrong MongoDB connection string
- Port configuration (Railway uses $PORT automatically)

### Issue: App still shows "Network Error"
**Solution:**
- Verify the Railway URL is accessible in browser
- Check that you updated app.json with correct URL
- Make sure you rebuilt the app after changing app.json

### Issue: Database connection failed
**Solution:**
- Verify MongoDB Atlas allows connections from anywhere (0.0.0.0/0)
- Check MONGO_URL is correct with password replaced
- Ensure database name is included in connection string

---

## Cost Breakdown

**MongoDB Atlas:**
- FREE (M0 tier) - 512MB storage
- Enough for thousands of users

**Railway:**
- $5 credit free trial
- Then ~$5-10/month depending on usage
- Estimated cost for your app: $5-7/month

**Total Monthly Cost: $5-7** (after free trial)

---

## Next Steps After Deployment

1. ✅ Backend is live on Railway
2. ✅ App connects successfully
3. ✅ All features working
4. Upload AAB to Google Play Console
5. Your app goes live! 🎉

---

## Important Notes

- Keep your Railway dashboard open to monitor deployments
- Railway auto-deploys when you push to GitHub
- Environment variables are encrypted and secure
- You can view logs in Railway dashboard for debugging
- Backend URL is permanent and won't change

---

## Need Help?

If you encounter any issues:
1. Check Railway deployment logs
2. Verify all environment variables are set
3. Test backend URL in browser first
4. Ensure MongoDB connection is working

Contact Railway support if deployment fails: https://railway.app/help
