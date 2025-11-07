FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-dev \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Buat copy requirements dan install Python packages
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Buat copy semua aplikasi Flask ke container
COPY app /app

EXPOSE 5000
CMD ["python", "app.py"]
