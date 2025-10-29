import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, StyleSheet, TouchableOpacity, TextInput, Alert, Modal, ActivityIndicator } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import Constants from 'expo-constants';

const BACKEND_URL = Constants.expoConfig?.extra?.backendUrl || process.env.EXPO_PUBLIC_BACKEND_URL || 'http://localhost:8001';

export default function AdminDashboard() {
  const [courses, setCourses] = useState<any[]>([]);
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [showAddModal, setShowAddModal] = useState(false);
  const [editingCourse, setEditingCourse] = useState<any>(null);
  const router = useRouter();

  // Form state
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [priceInr, setPriceInr] = useState('');
  const [thumbnail, setThumbnail] = useState('');
  const [category, setCategory] = useState('makeup');
  const [instructor, setInstructor] = useState('');
  const [duration, setDuration] = useState('');
  const [courseType, setCourseType] = useState('internal');
  const [externalUrl, setExternalUrl] = useState('');
  const [certificateEnabled, setCertificateEnabled] = useState(true);

  useEffect(() => {
    checkAuth();
    fetchData();
  }, []);

  const checkAuth = async () => {
    const token = await AsyncStorage.getItem('admin_token');
    if (!token) {
      router.replace('/admin/login');
    }
  };

  const fetchData = async () => {
    try {
      const token = await AsyncStorage.getItem('admin_token');
      
      // Fetch courses
      const coursesRes = await axios.get(`${BACKEND_URL}/api/courses`);
      setCourses(coursesRes.data);

      // Fetch stats
      const statsRes = await axios.get(`${BACKEND_URL}/api/admin/stats`, {
        headers: { Authorization: token }
      });
      setStats(statsRes.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = async () => {
    await AsyncStorage.removeItem('admin_token');
    await AsyncStorage.removeItem('admin_user');
    router.replace('/admin/login');
  };

  const openAddModal = () => {
    setEditingCourse(null);
    setTitle('');
    setDescription('');
    setPriceInr('');
    setThumbnail('');
    setCategory('makeup');
    setInstructor('');
    setDuration('');
    setCourseType('internal');
    setExternalUrl('');
    setCertificateEnabled(true);
    setShowAddModal(true);
  };

  const openEditModal = (course: any) => {
    setEditingCourse(course);
    setTitle(course.title);
    setDescription(course.description);
    setPriceInr(course.price_inr?.toString() || (course.price * 83).toString());
    setThumbnail(course.thumbnail);
    setCategory(course.category);
    setInstructor(course.instructor);
    setDuration(course.duration);
    setCourseType(course.course_type || 'internal');
    setExternalUrl(course.external_url || '');
    setCertificateEnabled(course.certificate_enabled !== false);
    setShowAddModal(true);
  };

  const handleSaveCourse = async () => {
    if (!title || !description || !priceInr) {
      Alert.alert('Error', 'Please fill all required fields');
      return;
    }

    // Validate external URL if course type is external
    if (courseType === 'external' && !externalUrl) {
      Alert.alert('Error', 'Please provide external URL for external courses');
      return;
    }

    try {
      const token = await AsyncStorage.getItem('admin_token');
      const courseData = {
        title,
        description,
        price_inr: parseFloat(priceInr),
        thumbnail: thumbnail || 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400',
        category,
        instructor: instructor || 'Irfana Begum',
        duration: duration || '4 weeks',
        lessons: [],
        course_type: courseType,
        external_url: externalUrl || null,
        certificate_enabled: certificateEnabled
      };

      if (editingCourse) {
        // Update existing course
        await axios.put(
          `${BACKEND_URL}/api/admin/courses/${editingCourse.id}`,
          courseData,
          { headers: { Authorization: token } }
        );
        Alert.alert('Success', 'Course updated successfully!');
      } else {
        // Create new course
        await axios.post(
          `${BACKEND_URL}/api/admin/courses`,
          courseData,
          { headers: { Authorization: token } }
        );
        Alert.alert('Success', 'Course created successfully!');
      }

      setShowAddModal(false);
      fetchData();
    } catch (error: any) {
      Alert.alert('Error', error.response?.data?.detail || 'Failed to save course');
    }
  };

  const handleDeleteCourse = async (courseId: string, courseTitle: string) => {
    Alert.alert(
      'Delete Course',
      `Are you sure you want to delete "${courseTitle}"?`,
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Delete',
          style: 'destructive',
          onPress: async () => {
            try {
              const token = await AsyncStorage.getItem('admin_token');
              await axios.delete(`${BACKEND_URL}/api/admin/courses/${courseId}`, {
                headers: { Authorization: token }
              });
              Alert.alert('Success', 'Course deleted successfully!');
              fetchData();
            } catch (error: any) {
              Alert.alert('Error', error.response?.data?.detail || 'Failed to delete course');
            }
          }
        }
      ]
    );
  };

  if (loading) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#FF1493" />
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <View>
          <Text style={styles.headerTitle}>Admin Dashboard</Text>
          <Text style={styles.headerSubtitle}>N&N Makeup Academy</Text>
        </View>
        <TouchableOpacity onPress={handleLogout} style={styles.logoutButton}>
          <Ionicons name="log-out-outline" size={24} color="#FF1493" />
        </TouchableOpacity>
      </View>

      <ScrollView style={styles.content}>
        {/* Stats Cards */}
        {stats && (
          <View style={styles.statsContainer}>
            <View style={styles.statCard}>
              <Ionicons name="book" size={32} color="#FF1493" />
              <Text style={styles.statValue}>{stats.total_courses}</Text>
              <Text style={styles.statLabel}>Courses</Text>
            </View>
            <View style={styles.statCard}>
              <Ionicons name="people" size={32} color="#4CAF50" />
              <Text style={styles.statValue}>{stats.total_users}</Text>
              <Text style={styles.statLabel}>Users</Text>
            </View>
            <View style={styles.statCard}>
              <Ionicons name="school" size={32} color="#2196F3" />
              <Text style={styles.statValue}>{stats.total_enrollments}</Text>
              <Text style={styles.statLabel}>Enrollments</Text>
            </View>
            <View style={styles.statCard}>
              <Ionicons name="cash" size={32} color="#FF9800" />
              <Text style={styles.statValue}>₹{stats.total_revenue_inr?.toFixed(0)}</Text>
              <Text style={styles.statLabel}>Revenue</Text>
            </View>
          </View>
        )}

        {/* Add Course Button */}
        <TouchableOpacity style={styles.addButton} onPress={openAddModal}>
          <Ionicons name="add-circle" size={24} color="#FFFFFF" />
          <Text style={styles.addButtonText}>Add New Course</Text>
        </TouchableOpacity>

        {/* Courses List */}
        <Text style={styles.sectionTitle}>All Courses</Text>
        {courses.map((course) => (
          <View key={course.id} style={styles.courseCard}>
            <View style={styles.courseHeader}>
              <View style={styles.courseInfo}>
                <Text style={styles.courseTitle}>{course.title}</Text>
                <Text style={styles.courseCategory}>{course.category.toUpperCase()}</Text>
              </View>
              <View style={styles.courseActions}>
                <TouchableOpacity onPress={() => openEditModal(course)} style={styles.actionButton}>
                  <Ionicons name="create-outline" size={24} color="#2196F3" />
                </TouchableOpacity>
                <TouchableOpacity 
                  onPress={() => handleDeleteCourse(course.id, course.title)} 
                  style={styles.actionButton}
                >
                  <Ionicons name="trash-outline" size={24} color="#F44336" />
                </TouchableOpacity>
              </View>
            </View>
            <Text style={styles.courseDescription} numberOfLines={2}>{course.description}</Text>
            <View style={styles.courseMeta}>
              <Text style={styles.coursePrice}>₹{course.price_inr || (course.price * 83).toFixed(0)}</Text>
              <Text style={styles.courseStudents}>{course.students_count} students</Text>
            </View>
          </View>
        ))}
      </ScrollView>

      {/* Add/Edit Course Modal */}
      <Modal
        visible={showAddModal}
        animationType="slide"
        onRequestClose={() => setShowAddModal(false)}
      >
        <SafeAreaView style={styles.modalContainer}>
          <View style={styles.modalHeader}>
            <Text style={styles.modalTitle}>
              {editingCourse ? 'Edit Course' : 'Add New Course'}
            </Text>
            <TouchableOpacity onPress={() => setShowAddModal(false)}>
              <Ionicons name="close" size={28} color="#333" />
            </TouchableOpacity>
          </View>

          <ScrollView style={styles.modalContent}>
            <Text style={styles.label}>Course Title *</Text>
            <TextInput
              style={styles.input}
              placeholder="Enter course title"
              value={title}
              onChangeText={setTitle}
              placeholderTextColor="#999"
            />

            <Text style={styles.label}>Description *</Text>
            <TextInput
              style={[styles.input, styles.textArea]}
              placeholder="Enter course description"
              value={description}
              onChangeText={setDescription}
              multiline
              numberOfLines={4}
              placeholderTextColor="#999"
            />

            <Text style={styles.label}>Price (₹) *</Text>
            <TextInput
              style={styles.input}
              placeholder="Enter price in rupees (e.g., 1000)"
              value={priceInr}
              onChangeText={setPriceInr}
              keyboardType="numeric"
              placeholderTextColor="#999"
            />

            <Text style={styles.label}>Category</Text>
            <View style={styles.categoryButtons}>
              {['makeup', 'nail', 'hair'].map((cat) => (
                <TouchableOpacity
                  key={cat}
                  style={[styles.categoryButton, category === cat && styles.categoryButtonActive]}
                  onPress={() => setCategory(cat)}
                >
                  <Text style={[styles.categoryButtonText, category === cat && styles.categoryButtonTextActive]}>
                    {cat.charAt(0).toUpperCase() + cat.slice(1)}
                  </Text>
                </TouchableOpacity>
              ))}
            </View>

            <Text style={styles.label}>Instructor</Text>
            <TextInput
              style={styles.input}
              placeholder="Instructor name"
              value={instructor}
              onChangeText={setInstructor}
              placeholderTextColor="#999"
            />

            <Text style={styles.label}>Duration</Text>
            <TextInput
              style={styles.input}
              placeholder="e.g., 4 weeks"
              value={duration}
              onChangeText={setDuration}
              placeholderTextColor="#999"
            />

            <Text style={styles.label}>Thumbnail URL (optional)</Text>
            <TextInput
              style={styles.input}
              placeholder="Image URL"
              value={thumbnail}
              onChangeText={setThumbnail}
              placeholderTextColor="#999"
            />

            <Text style={styles.label}>Course Type</Text>
            <View style={styles.categoryButtons}>
              <TouchableOpacity
                style={[styles.categoryButton, courseType === 'internal' && styles.categoryButtonActive]}
                onPress={() => setCourseType('internal')}
              >
                <Text style={[styles.categoryButtonText, courseType === 'internal' && styles.categoryButtonTextActive]}>
                  Internal (In-App)
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.categoryButton, courseType === 'external' && styles.categoryButtonActive]}
                onPress={() => setCourseType('external')}
              >
                <Text style={[styles.categoryButtonText, courseType === 'external' && styles.categoryButtonTextActive]}>
                  External (TagMango)
                </Text>
              </TouchableOpacity>
            </View>

            {courseType === 'external' && (
              <>
                <Text style={styles.label}>External URL (TagMango Link) *</Text>
                <TextInput
                  style={styles.input}
                  placeholder="e.g., https://learn.nnmua.com/l/..."
                  value={externalUrl}
                  onChangeText={setExternalUrl}
                  placeholderTextColor="#999"
                />
              </>
            )}

            <View style={styles.checkboxContainer}>
              <TouchableOpacity
                style={styles.checkbox}
                onPress={() => setCertificateEnabled(!certificateEnabled)}
              >
                {certificateEnabled && (
                  <Ionicons name="checkmark" size={18} color="#FF1493" />
                )}
              </TouchableOpacity>
              <Text style={styles.checkboxLabel}>
                Enable automatic certificate generation upon course completion
              </Text>
            </View>

            <TouchableOpacity style={styles.saveButton} onPress={handleSaveCourse}>
              <Text style={styles.saveButtonText}>
                {editingCourse ? 'Update Course' : 'Create Course'}
              </Text>
            </TouchableOpacity>
          </ScrollView>
        </SafeAreaView>
      </Modal>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#E0E0E0',
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#FF1493',
  },
  headerSubtitle: {
    fontSize: 14,
    color: '#666',
  },
  logoutButton: {
    padding: 8,
  },
  content: {
    flex: 1,
    padding: 20,
  },
  statsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginBottom: 20,
    gap: 12,
  },
  statCard: {
    flex: 1,
    minWidth: 150,
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  statValue: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#333',
    marginTop: 8,
  },
  statLabel: {
    fontSize: 14,
    color: '#666',
    marginTop: 4,
  },
  addButton: {
    flexDirection: 'row',
    backgroundColor: '#FF1493',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 20,
    elevation: 3,
    shadowColor: '#FF1493',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
  },
  addButtonText: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: 'bold',
    marginLeft: 8,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 16,
  },
  courseCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  courseHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: 8,
  },
  courseInfo: {
    flex: 1,
  },
  courseTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 4,
  },
  courseCategory: {
    fontSize: 12,
    color: '#FF1493',
    fontWeight: '600',
  },
  courseActions: {
    flexDirection: 'row',
  },
  actionButton: {
    padding: 8,
    marginLeft: 8,
  },
  courseDescription: {
    fontSize: 14,
    color: '#666',
    marginBottom: 12,
  },
  courseMeta: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  coursePrice: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#4CAF50',
  },
  courseStudents: {
    fontSize: 14,
    color: '#666',
  },
  modalContainer: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  modalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#E0E0E0',
  },
  modalTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#FF1493',
  },
  modalContent: {
    flex: 1,
    padding: 20,
  },
  label: {
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
    marginBottom: 8,
    marginTop: 16,
  },
  input: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#DDD',
    paddingHorizontal: 16,
    paddingVertical: 12,
    fontSize: 16,
    color: '#333',
  },
  textArea: {
    height: 100,
    textAlignVertical: 'top',
  },
  categoryButtons: {
    flexDirection: 'row',
    gap: 12,
  },
  categoryButton: {
    flex: 1,
    paddingVertical: 12,
    borderRadius: 8,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#DDD',
    alignItems: 'center',
  },
  categoryButtonActive: {
    backgroundColor: '#FF1493',
    borderColor: '#FF1493',
  },
  categoryButtonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#666',
  },
  categoryButtonTextActive: {
    color: '#FFFFFF',
  },
  saveButton: {
    backgroundColor: '#FF1493',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
    marginTop: 24,
    marginBottom: 40,
    elevation: 3,
    shadowColor: '#FF1493',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
  },
  saveButtonText: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
});
