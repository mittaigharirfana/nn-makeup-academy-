import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, StyleSheet, TouchableOpacity, Image, TextInput, ActivityIndicator, RefreshControl } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import api from '../../utils/api';

interface Course {
  id: string;
  title: string;
  description: string;
  price: number;
  thumbnail: string;
  category: string;
  instructor: string;
  duration: string;
  students_count: number;
}

export default function CoursesScreen() {
  const [courses, setCourses] = useState<Course[]>([]);
  const [filteredCourses, setFilteredCourses] = useState<Course[]>([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const router = useRouter();

  const categories = [
    { id: 'all', name: 'All' },
    { id: 'makeup', name: 'Makeup' },
    { id: 'nail', name: 'Nail Art' },
    { id: 'hair', name: 'Hair Styling' },
  ];

  useEffect(() => {
    fetchCourses();
  }, []);

  useEffect(() => {
    filterCourses();
  }, [courses, searchQuery, selectedCategory]);

  const fetchCourses = async () => {
    try {
      const response = await api.get('/courses');
      setCourses(response.data);
    } catch (error) {
      console.error('Error fetching courses:', error);
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  const onRefresh = () => {
    setRefreshing(true);
    fetchCourses();
  };

  const filterCourses = () => {
    let filtered = courses;

    // Filter by category
    if (selectedCategory !== 'all') {
      filtered = filtered.filter(course => course.category === selectedCategory);
    }

    // Filter by search query
    if (searchQuery) {
      filtered = filtered.filter(course =>
        course.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        course.description.toLowerCase().includes(searchQuery.toLowerCase())
      );
    }

    setFilteredCourses(filtered);
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
        <Text style={styles.title}>Explore Courses</Text>
        <Text style={styles.subtitle}>Master the art of beauty</Text>
      </View>

      <View style={styles.searchContainer}>
        <Ionicons name="search" size={20} color="#999" style={styles.searchIcon} />
        <TextInput
          style={styles.searchInput}
          placeholder="Search courses..."
          value={searchQuery}
          onChangeText={setSearchQuery}
          placeholderTextColor="#999"
        />
      </View>

      <ScrollView
        horizontal
        showsHorizontalScrollIndicator={false}
        style={styles.categoriesContainer}
        contentContainerStyle={styles.categoriesContent}
      >
        {categories.map(category => (
          <TouchableOpacity
            key={category.id}
            style={[
              styles.categoryChip,
              selectedCategory === category.id && styles.categoryChipActive
            ]}
            onPress={() => setSelectedCategory(category.id)}
          >
            <Text style={[
              styles.categoryText,
              selectedCategory === category.id && styles.categoryTextActive
            ]}>
              {category.name}
            </Text>
          </TouchableOpacity>
        ))}
      </ScrollView>

      <ScrollView
        style={styles.coursesContainer}
        showsVerticalScrollIndicator={false}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} colors={['#FF1493']} />
        }
      >
        <View style={styles.coursesGrid}>
          {filteredCourses.map(course => (
            <TouchableOpacity
              key={course.id}
              style={styles.courseCard}
              onPress={() => router.push({ pathname: '/course-detail', params: { id: course.id } })}
            >
              <Image source={{ uri: course.thumbnail }} style={styles.courseImage} />
              <View style={styles.courseContent}>
                <Text style={styles.courseTitle} numberOfLines={2}>{course.title}</Text>
                <Text style={styles.courseInstructor}>By {course.instructor}</Text>
                <View style={styles.courseFooter}>
                  <View style={styles.courseInfo}>
                    <Ionicons name="time-outline" size={14} color="#666" />
                    <Text style={styles.courseInfoText}>{course.duration}</Text>
                  </View>
                  <View style={styles.courseInfo}>
                    <Ionicons name="people-outline" size={14} color="#666" />
                    <Text style={styles.courseInfoText}>{course.students_count}+</Text>
                  </View>
                </View>
                <Text style={styles.coursePrice}>${course.price.toFixed(2)}</Text>
              </View>
            </TouchableOpacity>
          ))}
        </View>

        {filteredCourses.length === 0 && (
          <View style={styles.emptyContainer}>
            <Ionicons name="search-outline" size={64} color="#DDD" />
            <Text style={styles.emptyText}>No courses found</Text>
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
  searchContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    marginHorizontal: 20,
    borderRadius: 12,
    paddingHorizontal: 16,
    height: 48,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#FFE4E1',
  },
  searchIcon: {
    marginRight: 8,
  },
  searchInput: {
    flex: 1,
    fontSize: 16,
    color: '#333',
  },
  categoriesContainer: {
    maxHeight: 50,
    marginBottom: 16,
  },
  categoriesContent: {
    paddingHorizontal: 20,
  },
  categoryChip: {
    paddingHorizontal: 20,
    paddingVertical: 10,
    borderRadius: 20,
    backgroundColor: '#FFFFFF',
    marginRight: 12,
    borderWidth: 1,
    borderColor: '#FFE4E1',
  },
  categoryChipActive: {
    backgroundColor: '#FF1493',
    borderColor: '#FF1493',
  },
  categoryText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#666',
  },
  categoryTextActive: {
    color: '#FFFFFF',
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
    height: 180,
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
    marginBottom: 12,
  },
  courseFooter: {
    flexDirection: 'row',
    marginBottom: 12,
  },
  courseInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 16,
  },
  courseInfoText: {
    fontSize: 12,
    color: '#666',
    marginLeft: 4,
  },
  coursePrice: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#FF1493',
  },
  emptyContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    padding: 40,
  },
  emptyText: {
    fontSize: 16,
    color: '#999',
    marginTop: 16,
  },
});