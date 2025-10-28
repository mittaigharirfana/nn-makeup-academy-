import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, StyleSheet, TouchableOpacity, Image, ActivityIndicator, Alert } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import * as Linking from 'expo-linking';
import api from '../utils/api';

interface Lesson {
  id: string;
  title: string;
  description: string;
  video_url: string;
  duration: number;
  order: number;
}

interface CourseDetail {
  id: string;
  title: string;
  description: string;
  price: number;
  thumbnail: string;
  category: string;
  instructor: string;
  duration: string;
  students_count: number;
  lessons: Lesson[];
  progress?: number;
}

export default function CourseDetailScreen() {
  const [course, setCourse] = useState<CourseDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [enrolling, setEnrolling] = useState(false);
  const [isEnrolled, setIsEnrolled] = useState(false);
  const router = useRouter();
  const { id } = useLocalSearchParams<{ id: string }>();

  useEffect(() => {
    if (id) {
      console.log('Course ID:', id);
      fetchCourseDetails();
      checkEnrollment();
    } else {
      console.log('No course ID provided');
      setLoading(false);
    }
  }, [id]);

  const fetchCourseDetails = async () => {
    console.log('Fetching course details for ID:', id);
    try {
      const response = await api.get(`/courses/${id}`);
      console.log('Course data received:', response.data);
      setCourse(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching course details:', error);
      Alert.alert('Error', 'Failed to load course details');
      setLoading(false);
    }
  };

  const checkEnrollment = async () => {
    try {
      const response = await api.get('/my-courses');
      const enrolled = response.data.some((c: any) => c.id === id);
      setIsEnrolled(enrolled);
    } catch (error) {
      console.error('Error checking enrollment:', error);
    }
  };

  const handleEnroll = async () => {
    if (!course) return;

    setEnrolling(true);
    try {
      // Get origin URL
      const originUrl = Linking.createURL('');
      
      // Create checkout session
      const response = await api.post('/payment/create-checkout', {
        course_id: id,
        origin_url: originUrl.split('://')[1] ? originUrl : 'http://localhost:3000'
      });

      // Open Stripe checkout in browser
      if (response.data.url) {
        await Linking.openURL(response.data.url);
      }
    } catch (error: any) {
      Alert.alert('Error', error.response?.data?.detail || 'Failed to initiate payment');
    } finally {
      setEnrolling(false);
    }
  };

  const handlePlayLesson = (lesson: Lesson) => {
    router.push({
      pathname: '/video-player',
      params: {
        courseId: id!,
        lessonId: lesson.id,
        videoUrl: lesson.video_url,
        title: lesson.title
      }
    });
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

  if (!course) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <Text style={styles.errorText}>Course not found</Text>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container} edges={['bottom']}>
      <View style={styles.header}>
        <TouchableOpacity 
          style={styles.backButton}
          onPress={() => router.back()}
        >
          <Ionicons name="arrow-back" size={24} color="#333" />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>Course Details</Text>
        <View style={styles.placeholder} />
      </View>

      <ScrollView showsVerticalScrollIndicator={false}>
        <Image source={{ uri: course.thumbnail }} style={styles.thumbnail} />

        <View style={styles.content}>
          <View style={styles.categoryBadge}>
            <Text style={styles.categoryText}>{course.category.toUpperCase()}</Text>
          </View>

          <Text style={styles.title}>{course.title}</Text>
          <Text style={styles.instructor}>By {course.instructor}</Text>

          <View style={styles.stats}>
            <View style={styles.statItem}>
              <Ionicons name="time-outline" size={18} color="#666" />
              <Text style={styles.statText}>{course.duration}</Text>
            </View>
            <View style={styles.statItem}>
              <Ionicons name="people-outline" size={18} color="#666" />
              <Text style={styles.statText}>{course.students_count}+ students</Text>
            </View>
            <View style={styles.statItem}>
              <Ionicons name="videocam-outline" size={18} color="#666" />
              <Text style={styles.statText}>{course.lessons.length} lessons</Text>
            </View>
          </View>

          {isEnrolled && course.progress !== undefined && (
            <View style={styles.progressSection}>
              <Text style={styles.progressLabel}>Your Progress</Text>
              <View style={styles.progressBar}>
                <View style={[styles.progressFill, { width: `${course.progress}%` }]} />
              </View>
              <Text style={styles.progressText}>{Math.round(course.progress)}% complete</Text>
            </View>
          )}

          <View style={styles.section}>
            <Text style={styles.sectionTitle}>About this course</Text>
            <Text style={styles.description}>{course.description}</Text>
          </View>

          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Course Content</Text>
            {course.lessons.map((lesson, index) => (
              <TouchableOpacity
                key={lesson.id}
                style={styles.lessonCard}
                onPress={() => isEnrolled && handlePlayLesson(lesson)}
                disabled={!isEnrolled}
              >
                <View style={styles.lessonNumber}>
                  <Text style={styles.lessonNumberText}>{index + 1}</Text>
                </View>
                <View style={styles.lessonContent}>
                  <Text style={styles.lessonTitle}>{lesson.title}</Text>
                  <Text style={styles.lessonDescription} numberOfLines={1}>
                    {lesson.description}
                  </Text>
                  <View style={styles.lessonMeta}>
                    <Ionicons name="time-outline" size={14} color="#999" />
                    <Text style={styles.lessonDuration}>{lesson.duration} mins</Text>
                  </View>
                </View>
                {isEnrolled ? (
                  <Ionicons name="play-circle" size={32} color="#FF1493" />
                ) : (
                  <Ionicons name="lock-closed" size={24} color="#CCC" />
                )}
              </TouchableOpacity>
            ))}
          </View>
        </View>
      </ScrollView>

      {!isEnrolled && (
        <View style={styles.footer}>
          <View style={styles.priceContainer}>
            <Text style={styles.priceLabel}>Course Price</Text>
            <Text style={styles.price}>${course.price.toFixed(2)}</Text>
          </View>
          <TouchableOpacity 
            style={[styles.enrollButton, enrolling && styles.enrollButtonDisabled]}
            onPress={handleEnroll}
            disabled={enrolling}
          >
            <Text style={styles.enrollButtonText}>
              {enrolling ? 'Processing...' : 'Enroll Now'}
            </Text>
          </TouchableOpacity>
        </View>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFF5F7',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  errorText: {
    fontSize: 16,
    color: '#999',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 12,
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#F0F0F0',
  },
  backButton: {
    padding: 4,
  },
  headerTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  placeholder: {
    width: 32,
  },
  thumbnail: {
    width: '100%',
    height: 220,
    backgroundColor: '#F0F0F0',
  },
  content: {
    padding: 20,
  },
  categoryBadge: {
    alignSelf: 'flex-start',
    backgroundColor: '#FF1493',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 12,
    marginBottom: 12,
  },
  categoryText: {
    fontSize: 12,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 8,
  },
  instructor: {
    fontSize: 16,
    color: '#666',
    marginBottom: 16,
  },
  stats: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginBottom: 20,
  },
  statItem: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 20,
    marginBottom: 8,
  },
  statText: {
    fontSize: 14,
    color: '#666',
    marginLeft: 6,
  },
  progressSection: {
    backgroundColor: '#FFFFFF',
    padding: 16,
    borderRadius: 12,
    marginBottom: 20,
  },
  progressLabel: {
    fontSize: 14,
    fontWeight: '600',
    color: '#333',
    marginBottom: 8,
  },
  progressBar: {
    height: 8,
    backgroundColor: '#FFE4E1',
    borderRadius: 4,
    overflow: 'hidden',
    marginBottom: 6,
  },
  progressFill: {
    height: '100%',
    backgroundColor: '#FF1493',
  },
  progressText: {
    fontSize: 12,
    color: '#666',
  },
  section: {
    marginBottom: 24,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 12,
  },
  description: {
    fontSize: 15,
    color: '#666',
    lineHeight: 24,
  },
  lessonCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    padding: 16,
    borderRadius: 12,
    marginBottom: 12,
    elevation: 1,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.05,
    shadowRadius: 4,
  },
  lessonNumber: {
    width: 36,
    height: 36,
    borderRadius: 18,
    backgroundColor: '#FFF5F7',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  lessonNumberText: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#FF1493',
  },
  lessonContent: {
    flex: 1,
  },
  lessonTitle: {
    fontSize: 15,
    fontWeight: '600',
    color: '#333',
    marginBottom: 4,
  },
  lessonDescription: {
    fontSize: 13,
    color: '#999',
    marginBottom: 4,
  },
  lessonMeta: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  lessonDuration: {
    fontSize: 12,
    color: '#999',
    marginLeft: 4,
  },
  footer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    paddingHorizontal: 20,
    paddingVertical: 16,
    borderTopWidth: 1,
    borderTopColor: '#F0F0F0',
    elevation: 8,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: -2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
  },
  priceContainer: {
    flex: 1,
    marginRight: 16,
  },
  priceLabel: {
    fontSize: 12,
    color: '#666',
    marginBottom: 2,
  },
  price: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#FF1493',
  },
  enrollButton: {
    backgroundColor: '#FF1493',
    paddingHorizontal: 32,
    paddingVertical: 14,
    borderRadius: 12,
    elevation: 3,
    shadowColor: '#FF1493',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
  },
  enrollButtonDisabled: {
    opacity: 0.6,
  },
  enrollButtonText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
});