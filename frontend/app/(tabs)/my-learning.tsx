import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, StyleSheet, TouchableOpacity, Image, ActivityIndicator, RefreshControl } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import api from '../../utils/api';

interface EnrolledCourse {
  id: string;
  title: string;
  description: string;
  thumbnail: string;
  instructor: string;
  progress: number;
  enrollment_id: string;
}

export default function MyLearningScreen() {
  const [courses, setCourses] = useState<EnrolledCourse[]>([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const router = useRouter();

  useEffect(() => {
    fetchEnrolledCourses();
  }, []);

  const fetchEnrolledCourses = async () => {
    try {
      const response = await api.get('/my-courses');
      setCourses(response.data);
    } catch (error) {
      console.error('Error fetching enrolled courses:', error);
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  const onRefresh = () => {
    setRefreshing(true);
    fetchEnrolledCourses();
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
        <Text style={styles.title}>My Learning</Text>
        <Text style={styles.subtitle}>Continue your journey</Text>
      </View>

      <ScrollView
        style={styles.coursesContainer}
        showsVerticalScrollIndicator={false}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} colors={['#FF1493']} />
        }
      >
        {courses.length === 0 ? (
          <View style={styles.emptyContainer}>
            <Ionicons name="book-outline" size={80} color="#DDD" />
            <Text style={styles.emptyTitle}>No Courses Yet</Text>
            <Text style={styles.emptyText}>Start learning by enrolling in a course</Text>
            <TouchableOpacity 
              style={styles.browseButton}
              onPress={() => router.push('/(tabs)')}
            >
              <Text style={styles.browseButtonText}>Browse Courses</Text>
            </TouchableOpacity>
          </View>
        ) : (
          <View style={styles.coursesGrid}>
            {courses.map(course => (
              <TouchableOpacity
                key={course.id}
                style={styles.courseCard}
                onPress={() => router.push({ pathname: '/course-detail', params: { id: course.id } })}
              >
                <Image source={{ uri: course.thumbnail }} style={styles.courseImage} />
                <View style={styles.courseContent}>
                  <Text style={styles.courseTitle} numberOfLines={2}>{course.title}</Text>
                  <Text style={styles.courseInstructor}>By {course.instructor}</Text>
                  
                  <View style={styles.progressContainer}>
                    <View style={styles.progressBar}>
                      <View style={[styles.progressFill, { width: `${course.progress}%` }]} />
                    </View>
                    <Text style={styles.progressText}>{Math.round(course.progress)}% complete</Text>
                  </View>

                  <TouchableOpacity style={styles.continueButton}>
                    <Text style={styles.continueButtonText}>Continue Learning</Text>
                    <Ionicons name="play-circle" size={20} color="#FF1493" />
                  </TouchableOpacity>
                </View>
              </TouchableOpacity>
            ))}
          </View>
        )}
      </ScrollView>
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
  header: {
    padding: 20,
    paddingBottom: 16,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#FF1493',
    marginBottom: 4,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
  },
  coursesContainer: {
    flex: 1,
  },
  coursesGrid: {
    padding: 20,
    paddingTop: 0,
  },
  courseCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    marginBottom: 20,
    overflow: 'hidden',
    elevation: 3,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
  },
  courseImage: {
    width: '100%',
    height: 150,
    backgroundColor: '#F0F0F0',
  },
  courseContent: {
    padding: 16,
  },
  courseTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 4,
  },
  courseInstructor: {
    fontSize: 14,
    color: '#666',
    marginBottom: 16,
  },
  progressContainer: {
    marginBottom: 16,
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
    borderRadius: 4,
  },
  progressText: {
    fontSize: 12,
    color: '#666',
    fontWeight: '600',
  },
  continueButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#FFF5F7',
    paddingVertical: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#FF1493',
  },
  continueButtonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#FF1493',
    marginRight: 6,
  },
  emptyContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    padding: 40,
    marginTop: 60,
  },
  emptyTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginTop: 16,
    marginBottom: 8,
  },
  emptyText: {
    fontSize: 16,
    color: '#999',
    textAlign: 'center',
    marginBottom: 24,
  },
  browseButton: {
    backgroundColor: '#FF1493',
    paddingHorizontal: 32,
    paddingVertical: 14,
    borderRadius: 12,
  },
  browseButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
});