#!/bin/bash

echo "🔄 Restarting Backend with Fresh Code..."
echo ""

# Kill any existing backend processes
pkill -9 -f "uvicorn" 2>/dev/null
pkill -9 -f "app.main" 2>/dev/null
sleep 1

# Clear Python cache
echo "🧹 Clearing Python cache..."
find backend -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find backend -name "*.pyc" -delete 2>/dev/null

# Start backend
echo "🚀 Starting backend..."
cd backend
source venv/bin/activate
uvicorn app.main:app --port 8000 --reload

echo ""
echo "✅ Backend is running on http://localhost:8000"
echo "🛑 Press Ctrl+C to stop"
