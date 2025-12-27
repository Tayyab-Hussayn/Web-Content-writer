#!/bin/bash

# Function to handle cleanup on exit
cleanup() {
    echo -e "\nStopping servers..."
    if [ -n "$BACKEND_PID" ]; then
        kill $BACKEND_PID
    fi
    if [ -n "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID
    fi
    exit
}

# Trap SIGINT (Ctrl+C)
trap cleanup SIGINT

echo "🚀 Starting AI Content Writer..."

# Start Backend
echo "📦 Starting Backend Server (FastAPI)..."
cd backend
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found in backend/venv. Please run setup first."
    exit 1
fi

uvicorn app.main:app --port 8000 --reload &
BACKEND_PID=$!
cd ..

echo "⏳ Waiting 8 seconds for backend to initialize..."
sleep 8

# Start Frontend
echo "🎨 Starting Frontend Server (Next.js)..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo -e "\n✅ Services are running:"
echo "   - Backend: http://localhost:8000"
echo "   - Frontend: http://localhost:3000"
echo -e "\n🛑 Press Ctrl+C to stop all servers."

# Wait for processes
wait
