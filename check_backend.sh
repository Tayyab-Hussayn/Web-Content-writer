#!/bin/bash

echo "🔍 Checking if backend has latest code..."
echo ""

# Check if security.py has the fix
if grep -q "Bcrypt has a 72-byte limit" /home/krawin/code/Web-Content-Writer/backend/app/core/security.py; then
    echo "✅ security.py has the password truncation fix"
else
    echo "❌ security.py does NOT have the fix - this is the problem!"
    exit 1
fi

echo ""
echo "The code has the fix, but the backend server needs to reload."
echo ""
echo "Please do ONE of the following:"
echo ""
echo "Option 1: Touch the file to trigger auto-reload"
echo "  cd /home/krawin/code/Web-Content-Writer/backend"
echo "  touch app/core/security.py"
echo ""
echo "Option 2: Manually restart the backend"
echo "  # In the terminal running the backend, press Ctrl+C"
echo "  # Then run:"
echo "  cd /home/krawin/code/Web-Content-Writer/backend"
echo "  source venv/bin/activate"
echo "  uvicorn app.main:app --reload --port 8000"
echo ""
echo "After restarting, try registration again!"
