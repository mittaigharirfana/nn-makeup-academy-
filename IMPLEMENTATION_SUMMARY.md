# N&N Makeup Academy - External Courses & Certificates Implementation

## ✅ BACKEND COMPLETED

### 1. External Course Support

**Database Models Updated:**
- Added `course_type`: "internal" or "external"
- Added `external_url`: Link to TagMango or other platforms  
- Added `certificate_enabled`: Whether to auto-generate certificates

**Admin API Updated:**
- `POST /api/admin/courses` - Now accepts course_type, external_url, certificate_enabled
- `PUT /api/admin/courses/{id}` - Can update all new fields

### 2. Certificate System

**Auto-Generation:**
- Certificates automatically generated when progress reaches 100%
- Only for courses with `certificate_enabled: true`
- Unique certificate ID format: `NNAC-XXXX` (e.g., NNAC-A4F2)

**Certificate Fields:**
- Student Name
- Course Title
- Completion Date
- Certificate ID
- Issued Date

**New API Endpoints:**
- `GET /api/my-certificates` - Get all user certificates
- `GET /api/certificate/{certificate_id}` - Get specific certificate

---

## 🔄 TODO - FRONTEND IMPLEMENTATION

### 1. Admin Panel Updates Needed

**Add to Course Create/Edit Form:**
- [ ] Course Type selector (Internal / External)
- [ ] External URL input field (shown only if External)
- [ ] Certificate Enabled checkbox
- [ ] Show/hide lessons section based on course type

### 2. Course Display Updates

**Courses List (index.tsx):**
- [ ] Add badge for External courses (e.g., "🔗 External")
- [ ] Different styling for external courses

**Course Detail Page:**
- [ ] Check course_type
- [ ] If External: Show "Learn on TagMango" button → Opens external_url
- [ ] If Internal: Show "Enroll Now" button → Normal flow

### 3. Certificate Display

**Profile Screen:**
- [ ] Add "My Certificates" section
- [ ] List all earned certificates
- [ ] Show certificate ID, course name, date
- [ ] "View Certificate" button

**Certificate Screen (New):**
- [ ] Create `/certificate-detail.tsx` screen
- [ ] Beautiful certificate design with:
  - N&N Academy Logo/Branding
  - Student Name
  - Course Title
  - Completion Date
  - Certificate ID
  - Instructor signature (image)
- [ ] Download/Share option

**My Learning Screen:**
- [ ] Show certificate badge on completed courses
- [ ] "View Certificate" button for 100% completed courses

---

## 📊 How It Works

### External Courses Flow:
1. Admin adds course with type="external" and TagMango URL
2. Course shows in app with "External" badge
3. User clicks course → sees details
4. "Learn on TagMango" button opens external link
5. No video lessons shown for external courses

### Certificate Flow:
1. User enrolls in course (internal type)
2. User watches videos, progress tracked
3. When progress reaches 100%:
   - Backend auto-generates certificate
   - Certificate saved in database
   - User can view in Profile
4. User can view/download certificate anytime

---

## 🎯 Next Steps

**Priority 1: Admin Panel**
- Update admin dashboard to add external course fields
- Test adding TagMango course

**Priority 2: Course Display**
- Update course detail to handle external courses
- Add external URL button

**Priority 3: Certificates**
- Create certificate display UI
- Add to profile section
- Design certificate template

**Would you like me to proceed with these frontend implementations?**
