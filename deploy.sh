#!/bin/bash
# QRMaker Deployment Script

echo "🚀 QRMaker Deployment Script"
echo "=============================="

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: app.py not found. Please run this script from the project root."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Test the application locally
echo "🧪 Testing application..."
python -m flask run --host=127.0.0.1 --port=5000 &
SERVER_PID=$!

# Wait for server to start
sleep 3

# Check if server is running
if curl -s http://127.0.0.1:5000/health > /dev/null; then
    echo "✅ Application is running successfully!"
    echo "🌐 Local server: http://127.0.0.1:5000"
else
    echo "❌ Application failed to start"
fi

# Kill the test server
kill $SERVER_PID 2>/dev/null

echo ""
echo "📋 Deployment Options:"
echo "1. Vercel: vercel --prod"
echo "2. Heroku: git push heroku main"
echo "3. Local: python app.py"
echo ""
echo "✨ Happy coding!"
