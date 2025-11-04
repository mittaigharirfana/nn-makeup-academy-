#!/usr/bin/env python3
"""
N&N Makeup Academy Backend Testing - External Courses & Certificates
Testing comprehensive backend functionality for external course support and certificate system.
"""

import requests
import json
import sys
from datetime import datetime

# Backend URL from frontend .env
BACKEND_URL = "https://beauty-course-app.preview.emergentagent.com/api"

class BackendTester:
    def __init__(self):
        self.session = requests.Session()
        self.auth_token = None
        self.admin_token = None
        self.test_phone = "9876543210"
        self.external_course_id = None
        self.results = {
            "admin_auth": {"status": "pending", "details": []},
            "user_auth": {"status": "pending", "details": []},
            "external_course_creation": {"status": "pending", "details": []},
            "external_course_retrieval": {"status": "pending", "details": []},
            "certificate_apis": {"status": "pending", "details": []},
            "regression_tests": {"status": "pending", "details": []}
        }
    
    def log_result(self, category, message, success=True):
        """Log test result"""
        status = "✅" if success else "❌"
        print(f"{status} {category}: {message}")
        self.results[category]["details"].append({
            "message": message,
            "success": success,
            "timestamp": datetime.now().isoformat()
        })
    
    def test_admin_auth(self):
        """Test admin authentication"""
        print("\n=== Testing Admin Authentication ===")
        
        try:
            print("1. Testing admin login...")
            response = self.session.post(
                f"{BACKEND_URL}/admin/login",
                json={"username": "admin@nnacademy.com", "password": "Admin@123"},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code != 200:
                self.log_result("admin_auth", f"Admin login failed: {response.status_code} - {response.text}", False)
                self.results["admin_auth"]["status"] = "failed"
                return False
            
            admin_data = response.json()
            if not admin_data.get("success"):
                self.log_result("admin_auth", f"Admin login response invalid: {admin_data}", False)
                self.results["admin_auth"]["status"] = "failed"
                return False
            
            self.admin_token = admin_data.get("token")
            if not self.admin_token:
                self.log_result("admin_auth", "Admin token not found in response", False)
                self.results["admin_auth"]["status"] = "failed"
                return False
            
            self.log_result("admin_auth", f"Admin authentication successful, token: {self.admin_token[:15]}...")
            self.results["admin_auth"]["status"] = "passed"
            return True
            
        except Exception as e:
            self.log_result("admin_auth", f"Admin authentication error: {str(e)}", False)
            self.results["admin_auth"]["status"] = "failed"
            return False
    
    def test_user_auth(self):
        """Test user authentication flow: send OTP -> verify OTP"""
        print("\n=== Testing User Authentication ===")
        
        try:
            # Step 1: Send OTP
            print(f"1. Sending OTP to {self.test_phone}...")
            response = self.session.post(
                f"{BACKEND_URL}/auth/send-otp",
                json={"phone": self.test_phone},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code != 200:
                self.log_result("user_auth", f"Send OTP failed: {response.status_code} - {response.text}", False)
                self.results["user_auth"]["status"] = "failed"
                return False
            
            otp_data = response.json()
            if not otp_data.get("success"):
                self.log_result("user_auth", f"Send OTP response invalid: {otp_data}", False)
                self.results["user_auth"]["status"] = "failed"
                return False
            
            # Extract OTP from response (development mode)
            otp = otp_data.get("otp")
            if not otp:
                self.log_result("user_auth", "OTP not found in response", False)
                self.results["user_auth"]["status"] = "failed"
                return False
            
            self.log_result("user_auth", f"OTP sent successfully: {otp}")
            
            # Step 2: Verify OTP
            print(f"2. Verifying OTP: {otp}...")
            response = self.session.post(
                f"{BACKEND_URL}/auth/verify-otp",
                json={"phone": self.test_phone, "otp": otp},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code != 200:
                self.log_result("user_auth", f"Verify OTP failed: {response.status_code} - {response.text}", False)
                self.results["user_auth"]["status"] = "failed"
                return False
            
            verify_data = response.json()
            if not verify_data.get("success"):
                self.log_result("user_auth", f"Verify OTP response invalid: {verify_data}", False)
                self.results["user_auth"]["status"] = "failed"
                return False
            
            # Extract token
            self.auth_token = verify_data.get("token")
            if not self.auth_token:
                self.log_result("user_auth", "Token not found in verify response", False)
                self.results["user_auth"]["status"] = "failed"
                return False
            
            self.log_result("user_auth", f"User authentication successful, token: {self.auth_token[:10]}...")
            self.results["user_auth"]["status"] = "passed"
            return True
            
        except Exception as e:
            self.log_result("user_auth", f"User authentication error: {str(e)}", False)
            self.results["user_auth"]["status"] = "failed"
            return False
    
    def test_create_external_course(self):
        """Test creating an external course via admin API"""
        print("\n=== Testing External Course Creation ===")
        
        if not self.admin_token:
            self.log_result("external_course_creation", "No admin token available", False)
            self.results["external_course_creation"]["status"] = "failed"
            return False
        
        external_course_data = {
            "title": "Professional Certification Program",
            "description": "Full certification on TagMango platform",
            "price_inr": 42000,
            "category": "Professional",
            "instructor": "Irfana Begum",
            "duration": "12 weeks",
            "course_type": "external",
            "external_url": "https://learn.nnmua.com/l/d8ee974108",
            "certificate_enabled": False,
            "thumbnail": "https://images.unsplash.com/photo-1487412947147-5cebf100ffc2"
        }
        
        try:
            print("1. Creating external course via POST /api/admin/courses...")
            headers = {"Authorization": self.admin_token, "Content-Type": "application/json"}
            response = self.session.post(f"{BACKEND_URL}/admin/courses", 
                                       json=external_course_data, 
                                       headers=headers)
            
            if response.status_code != 200:
                self.log_result("external_course_creation", f"Create external course failed: {response.status_code} - {response.text}", False)
                self.results["external_course_creation"]["status"] = "failed"
                return False
            
            data = response.json()
            if not data.get("success"):
                self.log_result("external_course_creation", f"Create course response invalid: {data}", False)
                self.results["external_course_creation"]["status"] = "failed"
                return False
            
            course = data.get("course", {})
            self.external_course_id = course.get("id")
            
            # Verify all required fields
            checks = [
                ("title", course.get("title") == "Professional Certification Program"),
                ("price_inr", course.get("price_inr") == 42000),
                ("course_type", course.get("course_type") == "external"),
                ("external_url", course.get("external_url") == "https://learn.nnmua.com/l/d8ee974108"),
                ("certificate_enabled", course.get("certificate_enabled") == False),
                ("course_id", self.external_course_id is not None)
            ]
            
            all_passed = all(check[1] for check in checks)
            failed_checks = [check[0] for check in checks if not check[1]]
            
            if all_passed:
                self.log_result("external_course_creation", f"External course created successfully. ID: {self.external_course_id}")
                self.results["external_course_creation"]["status"] = "passed"
                return True
            else:
                self.log_result("external_course_creation", f"External course creation failed checks: {failed_checks}", False)
                self.results["external_course_creation"]["status"] = "failed"
                return False
                
        except Exception as e:
            self.log_result("external_course_creation", f"External course creation error: {str(e)}", False)
            self.results["external_course_creation"]["status"] = "failed"
            return False
    
    def test_external_course_retrieval(self):
        """Test retrieving external course via GET APIs"""
        print("\n=== Testing External Course Retrieval ===")
        
        try:
            # Test 1: GET /api/courses should include external course
            print("1. Testing GET /api/courses includes external course...")
            response = self.session.get(f"{BACKEND_URL}/courses")
            
            if response.status_code != 200:
                self.log_result("external_course_retrieval", f"GET courses failed: {response.status_code}", False)
                self.results["external_course_retrieval"]["status"] = "failed"
                return False
            
            courses = response.json()
            total_courses = len(courses)
            
            # Check for external course
            external_course_found = False
            if self.external_course_id:
                for course in courses:
                    if course.get("id") == self.external_course_id:
                        external_course_found = True
                        if (course.get("course_type") == "external" and 
                            course.get("external_url") == "https://learn.nnmua.com/l/d8ee974108"):
                            self.log_result("external_course_retrieval", f"External course found in courses list (Total: {total_courses})")
                        else:
                            self.log_result("external_course_retrieval", "External course found but missing required fields", False)
                            self.results["external_course_retrieval"]["status"] = "failed"
                            return False
                        break
                
                if not external_course_found:
                    self.log_result("external_course_retrieval", f"External course not found in courses list (Total: {total_courses})", False)
                    self.results["external_course_retrieval"]["status"] = "failed"
                    return False
            
            # Test 2: GET /api/courses/{external_course_id}
            if self.external_course_id:
                print(f"2. Testing GET /api/courses/{self.external_course_id}...")
                response = self.session.get(f"{BACKEND_URL}/courses/{self.external_course_id}")
                
                if response.status_code != 200:
                    self.log_result("external_course_retrieval", f"GET external course by ID failed: {response.status_code}", False)
                    self.results["external_course_retrieval"]["status"] = "failed"
                    return False
                
                course = response.json()
                
                # Verify external course specific fields
                required_fields = ["course_type", "external_url", "certificate_enabled"]
                missing_fields = [field for field in required_fields if field not in course]
                
                if missing_fields:
                    self.log_result("external_course_retrieval", f"External course missing fields: {missing_fields}", False)
                    self.results["external_course_retrieval"]["status"] = "failed"
                    return False
                
                if (course.get("course_type") == "external" and 
                    course.get("external_url") and
                    course.get("certificate_enabled") == False):
                    self.log_result("external_course_retrieval", "External course details verified successfully")
                else:
                    self.log_result("external_course_retrieval", "External course has incorrect field values", False)
                    self.results["external_course_retrieval"]["status"] = "failed"
                    return False
            
            self.results["external_course_retrieval"]["status"] = "passed"
            return True
            
        except Exception as e:
            self.log_result("external_course_retrieval", f"External course retrieval error: {str(e)}", False)
            self.results["external_course_retrieval"]["status"] = "failed"
            return False
    
    def test_certificate_apis(self):
        """Test certificate API endpoints"""
        print("\n=== Testing Certificate APIs ===")
        
        if not self.auth_token:
            self.log_result("certificate_apis", "No user token available for certificate testing", False)
            self.results["certificate_apis"]["status"] = "failed"
            return False
        
        try:
            # Test 1: GET /api/my-certificates with authentication
            print("1. Testing GET /api/my-certificates with authentication...")
            headers = {"Authorization": f"Bearer {self.auth_token}"}
            response = self.session.get(f"{BACKEND_URL}/my-certificates", headers=headers)
            
            if response.status_code != 200:
                self.log_result("certificate_apis", f"GET my-certificates failed: {response.status_code} - {response.text}", False)
                self.results["certificate_apis"]["status"] = "failed"
                return False
            
            certificates = response.json()
            if not isinstance(certificates, list):
                self.log_result("certificate_apis", f"My certificates response not a list: {type(certificates)}", False)
                self.results["certificate_apis"]["status"] = "failed"
                return False
            
            self.log_result("certificate_apis", f"GET my-certificates successful: {len(certificates)} certificates (expected for new user)")
            
            # Test 2: GET /api/my-certificates without authentication
            print("2. Testing GET /api/my-certificates without authentication...")
            response = self.session.get(f"{BACKEND_URL}/my-certificates")
            
            if response.status_code == 401:
                self.log_result("certificate_apis", "Correctly rejected unauthenticated request to my-certificates")
            else:
                self.log_result("certificate_apis", f"Expected 401 for unauthenticated request, got {response.status_code}", False)
                self.results["certificate_apis"]["status"] = "failed"
                return False
            
            # Test 3: GET /api/certificate/{certificate_id} with non-existent ID
            print("3. Testing GET /api/certificate/{certificate_id} with non-existent ID...")
            fake_cert_id = "NNAC-FAKE123"
            response = self.session.get(f"{BACKEND_URL}/certificate/{fake_cert_id}")
            
            if response.status_code == 404:
                self.log_result("certificate_apis", "Correctly returned 404 for non-existent certificate")
            else:
                self.log_result("certificate_apis", f"Expected 404 for non-existent certificate, got {response.status_code}", False)
                self.results["certificate_apis"]["status"] = "failed"
                return False
            
            self.results["certificate_apis"]["status"] = "passed"
            return True
            
        except Exception as e:
            self.log_result("certificate_apis", f"Certificate APIs error: {str(e)}", False)
            self.results["certificate_apis"]["status"] = "failed"
            return False
    
    def test_regression_features(self):
        """Test existing features regression"""
        print("\n=== Testing Existing Features Regression ===")
        
        try:
            # Test 1: Verify GET /api/courses returns all courses including new external course
            print("1. Testing GET /api/courses returns all courses...")
            response = self.session.get(f"{BACKEND_URL}/courses")
            
            if response.status_code != 200:
                self.log_result("regression_tests", f"GET courses failed: {response.status_code}", False)
                self.results["regression_tests"]["status"] = "failed"
                return False
            
            courses = response.json()
            total_courses = len(courses)
            
            # Should have at least 17 internal courses + 1 external course = 18
            if total_courses < 18:
                self.log_result("regression_tests", f"Expected at least 18 courses (17 internal + 1 external), got {total_courses}", False)
                self.results["regression_tests"]["status"] = "failed"
                return False
            
            self.log_result("regression_tests", f"GET courses returned {total_courses} courses (≥18 expected)")
            
            # Test 2: Verify course structure includes new fields (at least for some courses)
            print("2. Testing course structure includes new fields...")
            if not courses:
                self.log_result("regression_tests", "No courses found for structure test", False)
                self.results["regression_tests"]["status"] = "failed"
                return False
            
            # Check if at least one course (the external course we created) has the new fields
            required_fields = ["course_type", "external_url", "certificate_enabled", "price_inr"]
            courses_with_new_fields = []
            
            for course in courses:
                has_all_fields = all(field in course for field in required_fields)
                if has_all_fields:
                    courses_with_new_fields.append(course.get('title', 'Unknown'))
            
            if len(courses_with_new_fields) == 0:
                self.log_result("regression_tests", f"No courses have the new fields: {required_fields}", False)
                self.results["regression_tests"]["status"] = "failed"
                return False
            
            self.log_result("regression_tests", f"Course structure verified: {len(courses_with_new_fields)} courses have new fields including: {courses_with_new_fields[0]}")
            
            # Test 3: Verify price display in INR
            print("3. Testing price display in INR...")
            courses_with_inr = [c for c in courses if "price_inr" in c and c["price_inr"] is not None]
            
            if len(courses_with_inr) == 0:
                self.log_result("regression_tests", "No courses have price_inr field", False)
                self.results["regression_tests"]["status"] = "failed"
                return False
            
            self.log_result("regression_tests", f"Price display in INR working: {len(courses_with_inr)}/{len(courses)} courses have price_inr")
            
            self.results["regression_tests"]["status"] = "passed"
            return True
            
        except Exception as e:
            self.log_result("regression_tests", f"Regression tests error: {str(e)}", False)
            self.results["regression_tests"]["status"] = "failed"
            return False
    
    def run_all_tests(self):
        """Run all backend tests for External Courses & Certificates"""
        print(f"🚀 N&N MAKEUP ACADEMY BACKEND TESTING - EXTERNAL COURSES & CERTIFICATES")
        print(f"Backend URL: {BACKEND_URL}")
        print(f"Test started at: {datetime.now()}")
        print("=" * 80)
        
        # First, seed data if needed
        try:
            print("Seeding initial data...")
            response = self.session.post(f"{BACKEND_URL}/admin/seed-data")
            if response.status_code == 200:
                print("✅ Data seeded successfully")
            else:
                print(f"⚠️  Seed data response: {response.status_code}")
        except Exception as e:
            print(f"⚠️  Seed data error: {str(e)}")
        
        # Run tests in sequence
        tests = [
            ("Admin Authentication", self.test_admin_auth),
            ("User Authentication", self.test_user_auth),
            ("External Course Creation", self.test_create_external_course),
            ("External Course Retrieval", self.test_external_course_retrieval),
            ("Certificate APIs", self.test_certificate_apis),
            ("Existing Features Regression", self.test_regression_features)
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            if test_func():
                passed += 1
        
        # Print summary
        print("\n" + "=" * 80)
        print(f"🏁 TEST SUMMARY: {passed}/{total} tests passed")
        print("=" * 80)
        
        for category, result in self.results.items():
            status_icon = "✅" if result["status"] == "passed" else "❌" if result["status"] == "failed" else "⏳"
            category_name = category.replace('_', ' ').title()
            print(f"{status_icon} {category_name}: {result['status']}")
        
        if passed == total:
            print("\n🎉 ALL TESTS PASSED!")
            print("External Courses & Certificates features are working correctly!")
        else:
            print(f"\n⚠️  {total - passed} TEST(S) FAILED")
            print("Some features need attention.")
        
        return passed == total

if __name__ == "__main__":
    tester = BackendTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)