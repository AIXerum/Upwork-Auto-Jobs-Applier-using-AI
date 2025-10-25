# Deployment Guide - Hostinger Docker Container

Complete guide for deploying the Upwork Cover Letter Generator API to Hostinger using Docker.

## 🎯 Overview

This guide shows how to deploy the Python Flask backend as a Docker container on Hostinger, allowing your Chrome Extension or Electron App to connect from anywhere.

## 📋 Prerequisites

1. **Hostinger VPS Plan** with Docker support
2. **Domain name** (optional but recommended)
3. **API Keys** (Tavily, Gemini)
4. **SSH access** to your Hostinger VPS

## 🚀 Deployment Methods

### Method 1: Deploy via Docker Hub (Recommended)

#### Step 1: Build Docker Image Locally

```bash
# Navigate to project directory
cd /Users/chriscarter/Documents/GitHub/Upwork-Auto-Jobs-Applier-using-AI

# Build Docker image
docker build -t upwork-cover-letter-api:latest .

# Test locally first
docker run -p 5000:5000 --env-file .env upwork-cover-letter-api:latest
```

Visit `http://localhost:5000/health` to verify it works.

#### Step 2: Push to Docker Hub

```bash
# Tag image
docker tag upwork-cover-letter-api:latest YOUR_DOCKERHUB_USERNAME/upwork-cover-letter-api:latest

# Login to Docker Hub
docker login

# Push image
docker push YOUR_DOCKERHUB_USERNAME/upwork-cover-letter-api:latest
```

#### Step 3: Deploy to Hostinger VPS

```bash
# SSH into your Hostinger VPS
ssh root@YOUR_VPS_IP

# Pull and run the image
docker pull YOUR_DOCKERHUB_USERNAME/upwork-cover-letter-api:latest

# Create .env file on server
cat > .env << EOF
TAVILY_API_KEY=your_tavily_key
GEMINI_API_KEY=your_gemini_key
GROQ_API_KEY=your_groq_key
EOF

# Run container
docker run -d \
  --name upwork-api \
  --restart unless-stopped \
  -p 5000:5000 \
  --env-file .env \
  YOUR_DOCKERHUB_USERNAME/upwork-cover-letter-api:latest

# Check if running
docker ps
docker logs upwork-api
```

---

### Method 2: Deploy via Hostinger's Docker Manager

If Hostinger has a Docker management interface:

1. Upload Dockerfile to VPS
2. Use Hostinger panel to build image
3. Configure environment variables in panel
4. Deploy container through UI

---

### Method 3: Git + Build on Server

#### Step 1: Push Code to GitHub

```bash
# Initialize git repo (if not already)
git init
git add .
git commit -m "Add Docker deployment files"

# Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/upwork-cover-letter-api.git
git push -u origin main
```

#### Step 2: Deploy on Hostinger

```bash
# SSH to Hostinger VPS
ssh root@YOUR_VPS_IP

# Clone repository
git clone https://github.com/YOUR_USERNAME/upwork-cover-letter-api.git
cd upwork-cover-letter-api

# Create .env file
nano .env
# Add your API keys

# Build and run with Docker Compose
docker-compose up -d

# Check status
docker-compose ps
docker-compose logs -f
```

---

## 🔒 Security Best Practices

### 1. Use Environment Variables (Not .env in repo)

```bash
# On Hostinger VPS, set environment variables
export TAVILY_API_KEY="your_key"
export GEMINI_API_KEY="your_key"

# Or use Docker secrets
echo "your_api_key" | docker secret create gemini_key -
```

### 2. Enable HTTPS with Nginx Reverse Proxy

```bash
# Install Nginx on Hostinger
apt-get update && apt-get install -y nginx certbot python3-certbot-nginx

# Configure Nginx
cat > /etc/nginx/sites-available/upwork-api << EOF
server {
    listen 80;
    server_name api.yourdomain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Enable site
ln -s /etc/nginx/sites-available/upwork-api /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx

# Get SSL certificate
certbot --nginx -d api.yourdomain.com
```

### 3. Add CORS Restrictions

Edit `extension_server.py`:

```python
# Only allow specific origins
CORS(app, origins=["chrome-extension://YOUR_EXTENSION_ID"])
```

### 4. Add Rate Limiting

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

@app.route('/generate-cover-letter', methods=['POST'])
@limiter.limit("10 per minute")
def generate_cover_letter():
    # existing code
```

---

## 🔧 Managing the Container

### View Logs

```bash
docker logs upwork-api -f
```

### Restart Container

```bash
docker restart upwork-api
```

### Update to New Version

```bash
# Pull latest image
docker pull YOUR_DOCKERHUB_USERNAME/upwork-cover-letter-api:latest

# Stop old container
docker stop upwork-api
docker rm upwork-api

# Run new container
docker run -d --name upwork-api -p 5000:5000 --env-file .env YOUR_DOCKERHUB_USERNAME/upwork-cover-letter-api:latest
```

### Monitor Resources

```bash
docker stats upwork-api
```

---

## 🌐 Updating Chrome Extension for Production

After deploying to Hostinger, update the Chrome Extension:

1. Edit `chrome-extension/content.js`:

```javascript
// Change this line
const API_URL = 'https://api.yourdomain.com';  // Was 'http://localhost:5000'
```

2. Reload extension in Chrome
3. Test on Upwork job page

---

## 📊 Monitoring & Maintenance

### Health Check Endpoint

```bash
curl https://api.yourdomain.com/health
```

Should return:
```json
{
  "status": "ok",
  "message": "Server is running",
  "jobs_processed": 42
}
```

### Set Up Uptime Monitoring

Use services like:
- UptimeRobot (free)
- Pingdom
- StatusCake

Monitor: `https://api.yourdomain.com/health`

### Backup Strategy

```bash
# Backup generated cover letters
docker exec upwork-api tar czf /tmp/backup.tar.gz /app/files
docker cp upwork-api:/tmp/backup.tar.gz ./backups/
```

---

## 💰 Cost Estimates

### Hostinger VPS Pricing
- **VPS 1**: $4.99/month (1 vCPU, 4GB RAM) - ✅ Recommended
- **VPS 2**: $8.99/month (2 vCPU, 8GB RAM) - For high traffic

### API Costs
- **Gemini 2.0 Flash**: Free tier includes 1M tokens/month
- **Tavily API**: Free tier includes 1000 searches/month

**Estimated Total**: $5-10/month

---

## 🐛 Troubleshooting

### Container won't start

```bash
# Check logs
docker logs upwork-api

# Common issues:
# - Missing API keys in .env
# - Port 5000 already in use
# - Insufficient memory
```

### API unreachable from extension

1. Check firewall: `ufw allow 5000`
2. Verify CORS settings
3. Check Nginx configuration
4. Test with curl: `curl http://YOUR_VPS_IP:5000/health`

### Out of memory

```bash
# Increase container memory limit
docker run -d --memory="1g" --name upwork-api ...
```

---

## 📝 Production Checklist

- [ ] Docker image built and tested locally
- [ ] Image pushed to Docker Hub
- [ ] Container running on Hostinger VPS
- [ ] Environment variables configured
- [ ] Health check endpoint accessible
- [ ] HTTPS enabled with SSL certificate
- [ ] CORS configured for extension origin
- [ ] Rate limiting enabled
- [ ] Uptime monitoring configured
- [ ] Backup strategy implemented
- [ ] Chrome extension updated with production URL
- [ ] Extension tested with production API

---

## 🎉 Success!

Your Upwork Cover Letter Generator API is now running in production on Hostinger!

Users can now use the Chrome Extension or Electron App from anywhere to generate cover letters.

For support, check the main README or open an issue on GitHub.
