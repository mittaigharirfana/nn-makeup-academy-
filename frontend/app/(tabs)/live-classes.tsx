import React, { useState, useEffect } from 'react';
import { View, Text, ScrollView, StyleSheet, TouchableOpacity, Image, ActivityIndicator, RefreshControl, Alert } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import api from '../../utils/api';

interface LiveClass {
  id: string;
  title: string;
  description: string;
  date_time: string;
  instructor: string;
  max_participants: number;
  enrolled_users: string[];
  thumbnail: string;
  duration: number;
}

export default function LiveClassesScreen() {
  const [classes, setClasses] = useState<LiveClass[]>([]);
  const [myClasses, setMyClasses] = useState<LiveClass[]>([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [selectedTab, setSelectedTab] = useState<'upcoming' | 'my'>('upcoming');

  useEffect(() => {
    fetchLiveClasses();
  }, []);

  const fetchLiveClasses = async () => {
    try {
      const [upcomingResponse, myResponse] = await Promise.all([
        api.get('/live-classes'),
        api.get('/my-live-classes')
      ]);
      setClasses(upcomingResponse.data);
      setMyClasses(myResponse.data);
    } catch (error) {
      console.error('Error fetching live classes:', error);
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  const onRefresh = () => {
    setRefreshing(true);
    fetchLiveClasses();
  };

  const handleBookClass = async (classId: string) => {
    try {
      await api.post('/live-classes/book', { class_id: classId });
      Alert.alert('Success', 'Live class booked successfully!');
      fetchLiveClasses();
    } catch (error: any) {
      Alert.alert('Error', error.response?.data?.detail || 'Failed to book class');
    }
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
      month: 'short', 
      day: 'numeric', 
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
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

  const displayClasses = selectedTab === 'upcoming' ? classes : myClasses;

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Live Classes</Text>
        <Text style={styles.subtitle}>Join interactive sessions</Text>
      </View>

      <View style={styles.tabsContainer}>
        <TouchableOpacity
          style={[styles.tab, selectedTab === 'upcoming' && styles.tabActive]}
          onPress={() => setSelectedTab('upcoming')}
        >
          <Text style={[styles.tabText, selectedTab === 'upcoming' && styles.tabTextActive]}>
            Upcoming
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tab, selectedTab === 'my' && styles.tabActive]}
          onPress={() => setSelectedTab('my')}
        >
          <Text style={[styles.tabText, selectedTab === 'my' && styles.tabTextActive]}>
            My Classes
          </Text>
        </TouchableOpacity>
      </View>

      <ScrollView
        style={styles.classesContainer}
        showsVerticalScrollIndicator={false}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} colors={['#FF1493']} />
        }
      >
        {displayClasses.length === 0 ? (
          <View style={styles.emptyContainer}>
            <Ionicons name="videocam-outline" size={80} color="#DDD" />
            <Text style={styles.emptyTitle}>
              {selectedTab === 'upcoming' ? 'No Upcoming Classes' : 'No Booked Classes'}
            </Text>
            <Text style={styles.emptyText}>
              {selectedTab === 'upcoming' 
                ? 'Check back later for new live sessions'
                : 'Book a live class to get started'}
            </Text>
          </View>
        ) : (
          <View style={styles.classesGrid}>
            {displayClasses.map(liveClass => (
              <View key={liveClass.id} style={styles.classCard}>
                <Image source={{ uri: liveClass.thumbnail }} style={styles.classImage} />
                <View style={styles.classContent}>
                  <Text style={styles.classTitle} numberOfLines={2}>{liveClass.title}</Text>
                  <Text style={styles.classDescription} numberOfLines={2}>{liveClass.description}</Text>
                  
                  <View style={styles.classDetails}>
                    <View style={styles.classDetail}>
                      <Ionicons name="person-outline" size={16} color="#666" />
                      <Text style={styles.classDetailText}>{liveClass.instructor}</Text>
                    </View>
                    <View style={styles.classDetail}>
                      <Ionicons name="calendar-outline" size={16} color="#666" />
                      <Text style={styles.classDetailText}>{formatDate(liveClass.date_time)}</Text>
                    </View>
                    <View style={styles.classDetail}>
                      <Ionicons name="time-outline" size={16} color="#666" />
                      <Text style={styles.classDetailText}>{liveClass.duration} mins</Text>
                    </View>
                    <View style={styles.classDetail}>
                      <Ionicons name="people-outline" size={16} color="#666" />
                      <Text style={styles.classDetailText}>
                        {liveClass.enrolled_users.length}/{liveClass.max_participants}
                      </Text>
                    </View>
                  </View>

                  {selectedTab === 'upcoming' && (
                    <TouchableOpacity 
                      style={styles.bookButton}
                      onPress={() => handleBookClass(liveClass.id)}
                    >
                      <Ionicons name="calendar" size={18} color="#FFFFFF" />
                      <Text style={styles.bookButtonText}>Book Now</Text>
                    </TouchableOpacity>
                  )}

                  {selectedTab === 'my' && (
                    <View style={styles.bookedBadge}>
                      <Ionicons name="checkmark-circle" size={18} color="#4CAF50" />
                      <Text style={styles.bookedText}>Booked</Text>
                    </View>
                  )}
                </View>
              </View>
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
  tabsContainer: {
    flexDirection: 'row',
    marginHorizontal: 20,
    marginBottom: 16,
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 4,
  },
  tab: {
    flex: 1,
    paddingVertical: 12,
    alignItems: 'center',
    borderRadius: 10,
  },
  tabActive: {
    backgroundColor: '#FF1493',
  },
  tabText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#666',
  },
  tabTextActive: {
    color: '#FFFFFF',
  },
  classesContainer: {
    flex: 1,
  },
  classesGrid: {
    padding: 20,
    paddingTop: 0,
  },
  classCard: {
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
  classImage: {
    width: '100%',
    height: 150,
    backgroundColor: '#F0F0F0',
  },
  classContent: {
    padding: 16,
  },
  classTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 6,
  },
  classDescription: {
    fontSize: 14,
    color: '#666',
    marginBottom: 12,
  },
  classDetails: {
    marginBottom: 16,
  },
  classDetail: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 6,
  },
  classDetailText: {
    fontSize: 13,
    color: '#666',
    marginLeft: 6,
  },
  bookButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#FF1493',
    paddingVertical: 12,
    borderRadius: 8,
  },
  bookButtonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#FFFFFF',
    marginLeft: 6,
  },
  bookedBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#E8F5E9',
    paddingVertical: 12,
    borderRadius: 8,
  },
  bookedText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#4CAF50',
    marginLeft: 6,
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
  },
});