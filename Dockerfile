
FROM python:3.12.3-slim

WORKDIR /app

# Install system dependencies required for building packages
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libheif-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3", "heic2jpg.py"]


