import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, ActivityIndicator, TouchableOpacity, Share } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import api from '../utils/api';

interface Certificate {
  id: string;
  certificate_id: string;
  student_name: string;
  course_title: string;
  completion_date: string;
  issued_date: string;
}

export default function CertificateScreen() {
  const [certificate, setCertificate] = useState<Certificate | null>(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();
  const { id } = useLocalSearchParams<{ id: string }>();

  useEffect(() => {
    if (id) {
      fetchCertificate();
    }
  }, [id]);

  const fetchCertificate = async () => {
    try {
      const response = await api.get(`/certificate/${id}`);
      setCertificate(response.data);
    } catch (error) {
      console.error('Error fetching certificate:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleShare = async () => {
    if (!certificate) return;
    
    try {
      await Share.share({
        message: `🎓 I've completed "${certificate.course_title}" from N&N Makeup Academy! Certificate ID: ${certificate.certificate_id}`,
        title: 'My Certificate'
      });
    } catch (error) {
      console.error('Error sharing certificate:', error);
    }
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric' 
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

  if (!certificate) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.errorContainer}>
          <Ionicons name="alert-circle-outline" size={64} color="#FF1493" />
          <Text style={styles.errorText}>Certificate not found</Text>
          <TouchableOpacity 
            style={styles.backButton}
            onPress={() => router.back()}
          >
            <Text style={styles.backButtonText}>Go Back</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()}>
          <Ionicons name="arrow-back" size={24} color="#333" />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>Certificate</Text>
        <TouchableOpacity onPress={handleShare}>
          <Ionicons name="share-social-outline" size={24} color="#FF1493" />
        </TouchableOpacity>
      </View>

      <ScrollView style={styles.content}>
        {/* Certificate Card */}
        <View style={styles.certificateCard}>
          {/* Decorative Border */}
          <View style={styles.certificateBorder}>
            {/* Header Section */}
            <View style={styles.certificateHeader}>
              <Text style={styles.academyName}>N&N MAKEUP ACADEMY</Text>
              <Text style={styles.certificateTitle}>Certificate of Completion</Text>
            </View>

            {/* Decorative Line */}
            <View style={styles.decorativeLine} />

            {/* Content Section */}
            <View style={styles.certificateContent}>
              <Text style={styles.certifyText}>This is to certify that</Text>
              
              <Text style={styles.studentName}>{certificate.student_name}</Text>
              
              <Text style={styles.certifyText}>has successfully completed the course</Text>
              
              <Text style={styles.courseName}>{certificate.course_title}</Text>
              
              <Text style={styles.completionText}>
                on {formatDate(certificate.completion_date)}
              </Text>
            </View>

            {/* Footer Section */}
            <View style={styles.certificateFooter}>
              <View style={styles.signatureSection}>
                <View style={styles.signatureLine} />
                <Text style={styles.signatureLabel}>Irfana Begum</Text>
                <Text style={styles.signatureTitle}>Director & Chief Instructor</Text>
              </View>
            </View>

            {/* Certificate ID */}
            <View style={styles.certificateIdSection}>
              <Text style={styles.certificateIdLabel}>Certificate ID</Text>
              <Text style={styles.certificateId}>{certificate.certificate_id}</Text>
              <Text style={styles.issuedDate}>
                Issued on {formatDate(certificate.issued_date)}
              </Text>
            </View>
          </View>
        </View>

        {/* Actions */}
        <View style={styles.actions}>
          <TouchableOpacity 
            style={styles.shareButton}
            onPress={handleShare}
          >
            <Ionicons name="share-social" size={20} color="#FFF" style={{marginRight: 8}} />
            <Text style={styles.shareButtonText}>Share Certificate</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
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
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  errorText: {
    fontSize: 18,
    color: '#666',
    marginTop: 16,
    marginBottom: 24,
  },
  backButton: {
    backgroundColor: '#FF1493',
    paddingHorizontal: 24,
    paddingVertical: 12,
    borderRadius: 8,
  },
  backButtonText: {
    color: '#FFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 16,
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#E0E0E0',
  },
  headerTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  content: {
    flex: 1,
    padding: 20,
  },
  certificateCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 20,
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    marginBottom: 24,
  },
  certificateBorder: {
    borderWidth: 8,
    borderColor: '#FF1493',
    borderRadius: 12,
    padding: 24,
  },
  certificateHeader: {
    alignItems: 'center',
    marginBottom: 20,
  },
  academyName: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#FF1493',
    letterSpacing: 2,
    marginBottom: 8,
  },
  certificateTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    textAlign: 'center',
  },
  decorativeLine: {
    height: 2,
    backgroundColor: '#FFD700',
    marginVertical: 20,
  },
  certificateContent: {
    alignItems: 'center',
    paddingVertical: 20,
  },
  certifyText: {
    fontSize: 14,
    color: '#666',
    marginBottom: 12,
  },
  studentName: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#FF1493',
    marginVertical: 16,
    textAlign: 'center',
  },
  courseName: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginVertical: 16,
    textAlign: 'center',
  },
  completionText: {
    fontSize: 14,
    color: '#666',
    marginTop: 12,
  },
  certificateFooter: {
    marginTop: 40,
    alignItems: 'center',
  },
  signatureSection: {
    alignItems: 'center',
  },
  signatureLine: {
    width: 200,
    height: 2,
    backgroundColor: '#333',
    marginBottom: 8,
  },
  signatureLabel: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
  },
  signatureTitle: {
    fontSize: 12,
    color: '#666',
    marginTop: 4,
  },
  certificateIdSection: {
    alignItems: 'center',
    marginTop: 24,
    paddingTop: 20,
    borderTopWidth: 1,
    borderTopColor: '#E0E0E0',
  },
  certificateIdLabel: {
    fontSize: 12,
    color: '#999',
    marginBottom: 4,
  },
  certificateId: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#FF1493',
    letterSpacing: 1,
  },
  issuedDate: {
    fontSize: 12,
    color: '#999',
    marginTop: 8,
  },
  actions: {
    paddingBottom: 20,
  },
  shareButton: {
    backgroundColor: '#4CAF50',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 16,
    borderRadius: 12,
    elevation: 3,
    shadowColor: '#4CAF50',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
  },
  shareButtonText: {
    color: '#FFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
