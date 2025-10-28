import React, { useEffect } from 'react';
import { View, Text, StyleSheet, Image, ActivityIndicator } from 'react-native';
import { useRouter } from 'expo-router';
import { useAuth } from '../contexts/AuthContext';

export default function Index() {
  const router = useRouter();
  const { token, isLoading } = useAuth();

  useEffect(() => {
    if (!isLoading) {
      // Navigate based on auth status
      setTimeout(() => {
        if (token) {
          router.replace('/(tabs)');
        } else {
          router.replace('/auth/phone');
        }
      }, 1500);
    }
  }, [token, isLoading]);

  return (
    <View style={styles.container}>
      <View style={styles.content}>
        <Image
          source={require('../assets/images/app-image.png')}
          style={styles.logo}
          resizeMode="contain"
        />
        <Text style={styles.title}>N&N Makeup Academy</Text>
        <Text style={styles.subtitle}>Learn Makeup Artistry from Home</Text>
        <ActivityIndicator size="large" color="#FF69B4" style={styles.loader} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFF5F7',
    justifyContent: 'center',
    alignItems: 'center',
  },
  content: {
    alignItems: 'center',
    padding: 20,
  },
  logo: {
    width: 150,
    height: 150,
    marginBottom: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#FF1493',
    marginBottom: 8,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    marginBottom: 30,
    textAlign: 'center',
  },
  loader: {
    marginTop: 20,
  },
});