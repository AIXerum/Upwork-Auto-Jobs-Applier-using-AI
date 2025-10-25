# Upwork Cover Letter Generator - Docker Image
# For deploying the Python Flask server to Hostinger or any cloud provider

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir flask flask-cors gunicorn

# Copy application files
COPY src/ ./src/
COPY files/ ./files/
COPY extension_server.py .
COPY .env .

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=extension_server.py
ENV PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

# Run with Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120", "extension_server:app"]
