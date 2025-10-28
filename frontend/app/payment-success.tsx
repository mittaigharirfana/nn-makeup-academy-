import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ActivityIndicator, Alert } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import api from '../utils/api';

export default function PaymentSuccessScreen() {
  const [verifying, setVerifying] = useState(true);
  const [success, setSuccess] = useState(false);
  const router = useRouter();
  const { session_id } = useLocalSearchParams<{ session_id: string }>();

  useEffect(() => {
    if (session_id) {
      verifyPayment();
    }
  }, [session_id]);

  const verifyPayment = async () => {
    let attempts = 0;
    const maxAttempts = 5;
    const pollInterval = 2000; // 2 seconds

    const poll = async () => {
      try {
        const response = await api.get(`/payment/status/${session_id}`);
        
        if (response.data.status === 'success') {
          setSuccess(true);
          setVerifying(false);
          return;
        }

        attempts++;
        if (attempts < maxAttempts) {
          setTimeout(poll, pollInterval);
        } else {
          setVerifying(false);
          Alert.alert(
            'Payment Processing',
            'Your payment is being processed. Please check My Learning in a few minutes.',
            [{ text: 'OK', onPress: () => router.replace('/(tabs)') }]
          );
        }
      } catch (error: any) {
        setVerifying(false);
        Alert.alert('Error', 'Failed to verify payment status');
      }
    };

    poll();
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        {verifying ? (
          <>
            <ActivityIndicator size="large" color="#FF1493" />
            <Text style={styles.title}>Verifying Payment...</Text>
            <Text style={styles.subtitle}>Please wait while we confirm your enrollment</Text>
          </>
        ) : success ? (
          <>
            <View style={styles.iconContainer}>
              <Ionicons name="checkmark-circle" size={100} color="#4CAF50" />
            </View>
            <Text style={styles.successTitle}>Payment Successful!</Text>
            <Text style={styles.successSubtitle}>
              Congratulations! You have been successfully enrolled in the course.
            </Text>
            <TouchableOpacity 
              style={styles.button}
              onPress={() => router.replace('/(tabs)/my-learning')}
            >
              <Text style={styles.buttonText}>Start Learning</Text>
            </TouchableOpacity>
            <TouchableOpacity 
              style={styles.secondaryButton}
              onPress={() => router.replace('/(tabs)')}
            >
              <Text style={styles.secondaryButtonText}>Browse More Courses</Text>
            </TouchableOpacity>
          </>
        ) : (
          <>
            <View style={styles.iconContainer}>
              <Ionicons name="alert-circle" size={100} color="#FF9800" />
            </View>
            <Text style={styles.title}>Payment Processing</Text>
            <Text style={styles.subtitle}>
              Your payment is being processed. Please check My Learning in a few minutes.
            </Text>
            <TouchableOpacity 
              style={styles.button}
              onPress={() => router.replace('/(tabs)')}
            >
              <Text style={styles.buttonText}>Go to Home</Text>
            </TouchableOpacity>
          </>
        )}
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFF5F7',
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 32,
  },
  iconContainer: {
    marginBottom: 24,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginTop: 24,
    marginBottom: 12,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
    marginBottom: 32,
    lineHeight: 24,
  },
  successTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#4CAF50',
    marginBottom: 12,
    textAlign: 'center',
  },
  successSubtitle: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
    marginBottom: 32,
    lineHeight: 24,
  },
  button: {
    backgroundColor: '#FF1493',
    paddingHorizontal: 40,
    paddingVertical: 16,
    borderRadius: 12,
    marginBottom: 16,
    width: '100%',
    alignItems: 'center',
    elevation: 3,
    shadowColor: '#FF1493',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
  },
  buttonText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  secondaryButton: {
    paddingHorizontal: 40,
    paddingVertical: 16,
    borderRadius: 12,
    width: '100%',
    alignItems: 'center',
  },
  secondaryButtonText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#FF1493',
  },
});