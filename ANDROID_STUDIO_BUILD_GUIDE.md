# Building APK with Android Studio - Complete Guide

## Prerequisites

1. **Android Studio** installed on your computer
   - Download from: https://developer.android.com/studio

2. **Java JDK** (usually comes with Android Studio)

3. **Your project files** at: `C:\Users\ABDUL NAVEEN ANSARI\nn-makeup-academy`

---

## Step 1: Generate Native Android Project

Open Command Prompt in the **frontend** folder and run:

```bash
npx expo prebuild --platform android --clean
```

This will:
- Create an `android` folder with native Android code
- Configure the project for Android Studio
- Set up all necessary files

**Expected output**: You'll see "android" folder created in your frontend directory.

---

## Step 2: Open Project in Android Studio

1. **Launch Android Studio**

2. Click **File → Open**

3. Navigate to: `C:\Users\ABDUL NAVEEN ANSARI\nn-makeup-academy\frontend\android`

4. Click **OK**

5. **Wait for Gradle Sync** to complete (this may take 5-10 minutes the first time)
   - You'll see "Gradle sync in progress..." at the bottom
   - Wait until it says "Gradle sync successful"

---

## Step 3: Configure Build Settings

### A. Check Android SDK
1. Go to **File → Settings → Appearance & Behavior → System Settings → Android SDK**
2. Make sure these are installed:
   - ✅ Android SDK Platform 35
   - ✅ Android SDK Build-Tools 35.0.0
   - ✅ Android SDK Platform-Tools

### B. Update local.properties (if needed)
1. In Android Studio's Project view, find `local.properties`
2. Make sure it contains your SDK path:
   ```
   sdk.dir=C\:\\Users\\ABDUL NAVEEN ANSARI\\AppData\\Local\\Android\\Sdk
   ```

---

## Step 4: Create Keystore for Signing

### Option A: Use Existing Keystore (if you have one from previous apps)
Skip to Step 5 and use your existing keystore.

### Option B: Generate New Keystore

Open Command Prompt and run:

```bash
keytool -genkeypair -v -storetype PKCS12 -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000
```

**You'll be asked for:**
- Keystore password (remember this!)
- Your name and organization details
- Key password (can be same as keystore password)

**Save the keystore file** in a safe location and **NEVER lose it** - you'll need it for all future updates.

---

## Step 5: Configure Signing in Android Studio

### Method 1: Using Build → Generate Signed Bundle/APK

1. Click **Build → Generate Signed Bundle / APK**

2. Select **Android App Bundle (AAB)** for Play Store
   - Or select **APK** for direct installation

3. Click **Next**

4. **Create/Select Keystore**:
   - Click "Create new..." or "Choose existing..."
   - Fill in all fields:
     - Key store path
     - Key store password
     - Key alias
     - Key password

5. Click **Next**

6. **Select Build Variant**: `release`

7. Check **both V1 and V2 Signature**

8. Click **Finish**

### Method 2: Configure gradle.properties (Alternative)

1. Open `android/gradle.properties`

2. Add these lines:
   ```
   MYAPP_RELEASE_STORE_FILE=my-release-key.keystore
   MYAPP_RELEASE_KEY_ALIAS=my-key-alias
   MYAPP_RELEASE_STORE_PASSWORD=your_keystore_password
   MYAPP_RELEASE_KEY_PASSWORD=your_key_password
   ```

3. Open `android/app/build.gradle`

4. Add signing config:
   ```gradle
   android {
       ...
       signingConfigs {
           release {
               if (project.hasProperty('MYAPP_RELEASE_STORE_FILE')) {
                   storeFile file(MYAPP_RELEASE_STORE_FILE)
                   storePassword MYAPP_RELEASE_STORE_PASSWORD
                   keyAlias MYAPP_RELEASE_KEY_ALIAS
                   keyPassword MYAPP_RELEASE_KEY_PASSWORD
               }
           }
       }
       buildTypes {
           release {
               signingConfig signingConfigs.release
               ...
           }
       }
   }
   ```

---

## Step 6: Build the APK/AAB

### Using Android Studio GUI:
1. Go to **Build → Generate Signed Bundle / APK**
2. Follow the wizard (as described in Step 5)
3. Wait for build to complete (5-15 minutes)

### Using Command Line (faster):
```bash
cd android
./gradlew assembleRelease
```

For AAB (Play Store):
```bash
./gradlew bundleRelease
```

---

## Step 7: Locate Your Build

### APK Location:
```
frontend/android/app/build/outputs/apk/release/app-release.apk
```

### AAB Location (for Play Store):
```
frontend/android/app/build/outputs/bundle/release/app-release.aab
```

---

## Step 8: Test the APK

### Install on your phone:
1. Copy `app-release.apk` to your phone
2. Open file manager and tap the APK
3. Allow "Install from unknown sources" if prompted
4. Install and test!

### Or use ADB:
```bash
adb install app-release.apk
```

---

## Common Issues & Solutions

### Issue 1: "SDK location not found"
**Solution**: Create `local.properties` file in `android/` folder:
```
sdk.dir=C\:\\Users\\YOUR_USERNAME\\AppData\\Local\\Android\\Sdk
```

### Issue 2: "Gradle sync failed"
**Solution**: 
- Check internet connection
- Delete `android/.gradle` folder
- Click "Sync Project with Gradle Files" again

### Issue 3: "Execution failed for task ':app:lintVitalRelease'"
**Solution**: Add to `android/app/build.gradle`:
```gradle
android {
    lintOptions {
        checkReleaseBuilds false
        abortOnError false
    }
}
```

### Issue 4: Build takes too long
**Solution**: 
- Close other applications
- Increase Android Studio memory: Help → Edit Custom VM Options
  ```
  -Xmx4096m
  ```

---

## Next: Upload to Play Store

Once you have the AAB file:
1. Go to Google Play Console: https://play.google.com/console
2. Create a new app or select existing
3. Upload the AAB file
4. Fill in store listing, content rating, pricing
5. Submit for review

---

## Important Notes

1. **Keep your keystore safe** - you can't update your app without it
2. **Test thoroughly** before uploading to Play Store
3. **Increment version code** for each new build in `app.json`
4. **Use AAB** for Play Store (smaller download size)
5. **Use APK** for direct distribution or testing

---

## Need Help?

If you encounter any issues during the build process, note the specific error message and we can troubleshoot together.
