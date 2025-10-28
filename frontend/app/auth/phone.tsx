import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, KeyboardAvoidingView, Platform, ScrollView } from 'react-native';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { CustomAlert } from '../../components/CustomAlert';
import api from '../../utils/api';

export default function PhoneScreen() {
  const [phone, setPhone] = useState('');
  const [loading, setLoading] = useState(false);
  const [showAlert, setShowAlert] = useState(false);
  const [alertData, setAlertData] = useState({ title: '', message: '', otp: '' });
  const router = useRouter();

  const handleSendOTP = async () => {
    if (!phone || phone.length < 10) {
      setAlertData({
        title: 'Error',
        message: 'Please enter a valid 10-digit phone number',
        otp: ''
      });
      setShowAlert(true);
      return;
    }

    setLoading(true);
    try {
      console.log('Sending OTP for phone:', phone);
      const response = await api.post('/auth/send-otp', { phone });
      console.log('OTP Response:', response.data);
      
      if (response.data.success) {
        const otp = response.data.otp;
        console.log('OTP received:', otp);
        
        setAlertData({
          title: 'OTP Sent Successfully!',
          message: `Your OTP is: ${otp}\n\nPlease enter this code in the next screen.`,
          otp: otp
        });
        setShowAlert(true);
      }
    } catch (error: any) {
      console.error('Send OTP Error:', error);
      const errorMessage = error.response?.data?.detail || error.message || 'Failed to send OTP. Please check your connection.';
      setAlertData({
        title: 'Error',
        message: errorMessage,
        otp: ''
      });
      setShowAlert(true);
    } finally {
      setLoading(false);
    }
  };

  const handleAlertClose = () => {
    setShowAlert(false);
    if (alertData.otp) {
      // Navigate to verify screen
      router.push({ pathname: '/auth/verify', params: { phone, otp: alertData.otp } });
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <KeyboardAvoidingView 
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
        style={styles.keyboardView}
      >
        <ScrollView contentContainerStyle={styles.scrollContent}>
          <View style={styles.content}>
            <View style={styles.header}>
              <Text style={styles.title}>Welcome to</Text>
              <Text style={styles.brand}>N&N Makeup Academy</Text>
              <Text style={styles.subtitle}>Enter your phone number to get started</Text>
            </View>

            <View style={styles.form}>
              <Text style={styles.label}>Phone Number</Text>
              <View style={styles.inputContainer}>
                <Text style={styles.prefix}>+91</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Enter 10-digit number"
                  value={phone}
                  onChangeText={setPhone}
                  keyboardType="phone-pad"
                  maxLength={10}
                  placeholderTextColor="#999"
                />
              </View>

              <TouchableOpacity 
                style={[styles.button, loading && styles.buttonDisabled]}
                onPress={handleSendOTP}
                disabled={loading}
              >
                <Text style={styles.buttonText}>
                  {loading ? 'Sending...' : 'Send OTP'}
                </Text>
              </TouchableOpacity>
            </View>

            <Text style={styles.footer}>
              By continuing, you agree to our Terms of Service and Privacy Policy
            </Text>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>

      <CustomAlert
        visible={showAlert}
        title={alertData.title}
        message={alertData.message}
        onClose={handleAlertClose}
        confirmText="Continue"
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFF5F7',
  },
  keyboardView: {
    flex: 1,
  },
  scrollContent: {
    flexGrow: 1,
  },
  content: {
    flex: 1,
    padding: 24,
    justifyContent: 'center',
  },
  header: {
    marginBottom: 48,
  },
  title: {
    fontSize: 24,
    color: '#666',
    marginBottom: 4,
  },
  brand: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FF1493',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
  },
  form: {
    marginBottom: 32,
  },
  label: {
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
    marginBottom: 8,
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#FFB6C1',
    marginBottom: 24,
    paddingHorizontal: 16,
  },
  prefix: {
    fontSize: 18,
    fontWeight: '600',
    color: '#333',
    marginRight: 8,
  },
  input: {
    flex: 1,
    height: 56,
    fontSize: 18,
    color: '#333',
  },
  button: {
    backgroundColor: '#FF1493',
    borderRadius: 12,
    height: 56,
    justifyContent: 'center',
    alignItems: 'center',
    elevation: 3,
    shadowColor: '#FF1493',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
  footer: {
    fontSize: 12,
    color: '#999',
    textAlign: 'center',
    lineHeight: 18,
  },
});