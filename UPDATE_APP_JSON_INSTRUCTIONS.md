# Update app.json with Production Backend URL

## Your Production Backend URL:
```
https://beauty-course-app.emergent.host
```

## Steps to Update Your Local app.json:

### Step 1: Open app.json
Navigate to: `C:\Users\ABDUL NAVEEN ANSARI\nn-makeup-academy\frontend\app.json`

### Step 2: Add the Production URL
Find the section near the end of the file that looks like:

```json
    "experiments": {
      "typedRoutes": true
    }
  }
}
```

### Step 3: Replace with this:
```json
    "experiments": {
      "typedRoutes": true
    },
    "extra": {
      "backendUrl": "https://beauty-course-app.emergent.host"
    }
  }
}
```

**Important:** Add a comma after `}` on the "experiments" line, then add the "extra" section.

### Step 4: Save the file

---

## Now Rebuild Your APK:

Open Command Prompt in the frontend folder and run:

```bash
eas build --platform android --profile production
```

This will take 10-20 minutes. When done, you'll get a download link for your production-ready AAB file!

---

## What This Does:

- Your app will now connect to the permanent production backend
- All users will be able to use your app
- No more "Network Error" issues
- Ready for Google Play Store submission!
