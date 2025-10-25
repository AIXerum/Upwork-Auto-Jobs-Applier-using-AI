#!/bin/bash

# Deployment script for Hostinger VPS
# Usage: ./deploy.sh

set -e

echo "========================================================================"
echo "🚀 DEPLOYING UPWORK COVER LETTER API TO HOSTINGER VPS"
echo "========================================================================"

# Configuration
VPS_IP="46.202.93.22"
VPS_USER="root"
REMOTE_DIR="/opt/upwork-api"
IMAGE_NAME="upwork-cover-letter-api"

echo ""
echo "📡 VPS: $VPS_USER@$VPS_IP"
echo "📁 Remote directory: $REMOTE_DIR"
echo ""

# Step 1: Check SSH connection
echo "1️⃣  Testing SSH connection..."
if ssh -o ConnectTimeout=5 $VPS_USER@$VPS_IP "echo 'SSH connection successful'" 2>/dev/null; then
    echo "   ✅ SSH connection working"
else
    echo "   ❌ Cannot connect to VPS"
    echo "   💡 Make sure you can SSH: ssh $VPS_USER@$VPS_IP"
    exit 1
fi

# Step 2: Create deployment package
echo ""
echo "2️⃣  Creating deployment package..."
tar -czf deploy-package.tar.gz \
    --exclude='venv' \
    --exclude='node_modules' \
    --exclude='electron-app' \
    --exclude='chrome-extension' \
    --exclude='*.pyc' \
    --exclude='__pycache__' \
    --exclude='.git' \
    --exclude='*.log' \
    --exclude='logs' \
    --exclude='debug_*' \
    --exclude='test_*.py' \
    Dockerfile \
    docker-compose.yml \
    requirements.txt \
    extension_server.py \
    src/ \
    files/ \
    .env

echo "   ✅ Package created: deploy-package.tar.gz"

# Step 3: Upload to VPS
echo ""
echo "3️⃣  Uploading to VPS..."
scp deploy-package.tar.gz $VPS_USER@$VPS_IP:/tmp/

echo "   ✅ Files uploaded"

# Step 4: Deploy on VPS
echo ""
echo "4️⃣  Deploying on VPS..."

ssh $VPS_USER@$VPS_IP << 'ENDSSH'
set -e

echo "   📦 Extracting files..."
mkdir -p /opt/upwork-api
cd /opt/upwork-api
tar -xzf /tmp/deploy-package.tar.gz
rm /tmp/deploy-package.tar.gz

echo "   🐳 Checking Docker..."
if ! command -v docker &> /dev/null; then
    echo "   📥 Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    systemctl start docker
    systemctl enable docker
    rm get-docker.sh
    echo "   ✅ Docker installed"
else
    echo "   ✅ Docker already installed"
fi

echo "   🛑 Stopping old container (if exists)..."
docker stop upwork-api 2>/dev/null || true
docker rm upwork-api 2>/dev/null || true

echo "   🏗️  Building Docker image..."
docker build -t upwork-cover-letter-api:latest .

echo "   🚀 Starting container..."
docker run -d \
    --name upwork-api \
    --restart unless-stopped \
    -p 5000:5000 \
    --env-file .env \
    upwork-cover-letter-api:latest

echo "   ⏳ Waiting for container to be healthy..."
sleep 5

echo "   🔍 Checking container status..."
docker ps | grep upwork-api

echo ""
echo "   ✅ Container is running!"

ENDSSH

# Step 5: Test deployment
echo ""
echo "5️⃣  Testing API endpoint..."
sleep 2

if curl -f http://$VPS_IP:5000/health 2>/dev/null; then
    echo "   ✅ API is responding!"
else
    echo "   ⚠️  API not responding yet (may need a few more seconds)"
fi

# Cleanup
rm deploy-package.tar.gz

echo ""
echo "========================================================================"
echo "✅ DEPLOYMENT COMPLETE!"
echo "========================================================================"
echo ""
echo "🌐 API URL: http://$VPS_IP:5000"
echo ""
echo "📋 Next steps:"
echo "  1. Test: curl http://$VPS_IP:5000/health"
echo "  2. Update Chrome extension content.js:"
echo "     const API_URL = 'http://$VPS_IP:5000';"
echo "  3. Reload extension in Chrome"
echo "  4. Test on Upwork job page!"
echo ""
echo "📊 View logs: ssh $VPS_USER@$VPS_IP 'docker logs upwork-api -f'"
echo "🔄 Restart: ssh $VPS_USER@$VPS_IP 'docker restart upwork-api'"
echo "🛑 Stop: ssh $VPS_USER@$VPS_IP 'docker stop upwork-api'"
echo ""
echo "========================================================================"
