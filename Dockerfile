FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (minimal set)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libgomp1 \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY yolo11x.pt .
COPY templates/ ./templates/

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

