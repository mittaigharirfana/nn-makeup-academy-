#!/bin/bash
# N&N Makeup Academy - Rebuild Script

echo "🚀 Setting up N&N Makeup Academy..."

# Frontend setup
echo "📱 Setting up Frontend..."
cd frontend
npm install
echo "✅ Frontend dependencies installed"

# Backend setup  
echo "🔧 Setting up Backend..."
cd ../backend

# Create .env file
echo "📝 Creating .env file..."
cat > .env << 'EOF'
MONGO_URL="mongodb://localhost:27017"
DB_NAME="nnacademy_database"
RAZORPAY_KEY_ID=rzp_live_RbKBTYfMg8MDci
RAZORPAY_KEY_SECRET=5hF6YB26hB4kT7W8sr9mxJtO
TWILIO_ACCOUNT_SID=AC44f43f2a2d4cb5e8eaec8307ed29588b
TWILIO_AUTH_TOKEN=10623a066b0fc323b079fd7f7faa96ba
TWILIO_PHONE_NUMBER=+16602286999
ADMIN_USERNAME=admin@nnacademy.com
ADMIN_PASSWORD=Admin@123
EOF

echo "✅ Backend .env created"

pip install -r requirements.txt
echo "✅ Backend dependencies installed"

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To build for Play Store:"
echo "  cd frontend"
echo "  eas login"
echo "  eas build --platform android --profile production"
