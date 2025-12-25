#!/bin/bash

echo "🐘 PostgreSQL Setup Script for ContentAI"
echo "=========================================="
echo ""

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null; then
    echo "❌ PostgreSQL is not installed."
    echo ""
    echo "Please install PostgreSQL first:"
    echo "  Ubuntu/Debian: sudo apt update && sudo apt install postgresql postgresql-contrib"
    echo "  macOS: brew install postgresql"
    echo "  Fedora: sudo dnf install postgresql-server postgresql-contrib"
    echo ""
    exit 1
fi

echo "✅ PostgreSQL is installed"
echo ""

# Check if PostgreSQL service is running
if ! sudo systemctl is-active --quiet postgresql; then
    echo "⚠️  PostgreSQL service is not running. Starting it..."
    sudo systemctl start postgresql
    sudo systemctl enable postgresql
    echo "✅ PostgreSQL service started"
else
    echo "✅ PostgreSQL service is running"
fi

echo ""
echo "Creating database and user..."
echo ""

# Create database and user
sudo -u postgres psql << EOF
-- Drop database if exists (for clean setup)
DROP DATABASE IF EXISTS contentai;
DROP USER IF EXISTS contentai_user;

-- Create database
CREATE DATABASE contentai;

-- Create user (change password in production!)
CREATE USER contentai_user WITH PASSWORD 'contentai_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE contentai TO contentai_user;

-- For PostgreSQL 15+, grant schema privileges
\c contentai
GRANT ALL ON SCHEMA public TO contentai_user;

\q
EOF

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Database 'contentai' created successfully"
    echo "✅ User 'contentai_user' created successfully"
    echo ""
    echo "📝 Update your backend/.env file with:"
    echo "   DATABASE_URL=postgresql+asyncpg://contentai_user:contentai_password@localhost:5432/contentai"
    echo ""
    echo "⚠️  IMPORTANT: Change the password in production!"
    echo ""
else
    echo ""
    echo "❌ Failed to create database. Please check PostgreSQL logs."
    exit 1
fi

echo "🎉 PostgreSQL setup complete!"
echo ""
echo "Next steps:"
echo "1. Update backend/.env with the DATABASE_URL above"
echo "2. Install Python dependencies: cd backend && pip install -r requirements.txt"
echo "3. Start the backend: uvicorn app.main:app --reload --port 8000"
