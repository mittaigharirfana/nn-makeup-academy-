import React, { useState, useEffect, useRef } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ActivityIndicator, Alert, Linking } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import { WebView } from 'react-native-webview';
import * as WebBrowser from 'expo-web-browser';
import api from '../utils/api';

export default function VideoPlayerScreen() {
  const [loading, setLoading] = useState(true);
  const router = useRouter();
  const { courseId, lessonId, videoUrl, title } = useLocalSearchParams<{
    courseId: string;
    lessonId: string;
    videoUrl: string;
    title: string;
  }>();

  useEffect(() => {
    // Mark lesson as started
    markProgress();
  }, []);

  const markProgress = async () => {
    try {
      await api.post(`/courses/${courseId}/progress`, {
        lesson_id: lessonId
      });
    } catch (error) {
      console.error('Error updating progress:', error);
    }
  };

  const getEmbedUrl = (url: string) => {
    // Convert YouTube watch URL to embed URL
    if (url.includes('youtube.com/watch')) {
      const videoId = url.split('v=')[1]?.split('&')[0];
      return `https://www.youtube.com/embed/${videoId}`;
    }
    if (url.includes('youtu.be/')) {
      const videoId = url.split('youtu.be/')[1]?.split('?')[0];
      return `https://www.youtube.com/embed/${videoId}`;
    }
    return url;
  };

  const embedUrl = videoUrl ? getEmbedUrl(videoUrl) : '';

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <View style={styles.header}>
        <TouchableOpacity 
          style={styles.backButton}
          onPress={() => router.back()}
        >
          <Ionicons name="close" size={28} color="#333" />
        </TouchableOpacity>
        <Text style={styles.title} numberOfLines={1}>{title}</Text>
        <View style={styles.placeholder} />
      </View>

      <View style={styles.playerContainer}>
        {loading && (
          <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="#FF1493" />
          </View>
        )}
        <WebView
          source={{ uri: embedUrl }}
          style={styles.video}
          allowsFullscreenVideo
          onLoadStart={() => setLoading(true)}
          onLoadEnd={() => setLoading(false)}
          onError={() => {
            setLoading(false);
            Alert.alert('Error', 'Failed to load video');
          }}
        />
      </View>

      <View style={styles.info}>
        <Text style={styles.infoTitle}>Currently Watching</Text>
        <Text style={styles.infoDescription}>Mark this lesson as complete to track your progress</Text>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 12,
    backgroundColor: '#FFFFFF',
  },
  backButton: {
    padding: 4,
  },
  title: {
    flex: 1,
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
    textAlign: 'center',
    marginHorizontal: 12,
  },
  placeholder: {
    width: 36,
  },
  playerContainer: {
    width: '100%',
    aspectRatio: 16 / 9,
    backgroundColor: '#000',
    position: 'relative',
  },
  video: {
    flex: 1,
  },
  loadingContainer: {
    ...StyleSheet.absoluteFillObject,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#000',
    zIndex: 1,
  },
  info: {
    backgroundColor: '#FFFFFF',
    padding: 20,
    flex: 1,
  },
  infoTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 8,
  },
  infoDescription: {
    fontSize: 14,
    color: '#666',
    lineHeight: 20,
  },
});