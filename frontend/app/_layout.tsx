import { Stack } from 'expo-router';
import { AuthProvider } from '../src/contexts/AuthContext';
import { StatusBar } from 'expo-status-bar';

export default function RootLayout() {
  return (
    <AuthProvider>
      <StatusBar style="dark" />
      <Stack screenOptions={{ headerShown: false }}>
        <Stack.Screen name="index" />
        <Stack.Screen name="auth/phone" />
        <Stack.Screen name="auth/verify" />
        <Stack.Screen name="(tabs)" />
        <Stack.Screen name="course-detail" />
        <Stack.Screen name="video-player" />
        <Stack.Screen name="payment-success" />
        <Stack.Screen name="admin/login" />
        <Stack.Screen name="admin/dashboard" />
      </Stack>
    </AuthProvider>
  );
}