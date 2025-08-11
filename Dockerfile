FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create output directory
RUN mkdir -p output

# Copy the application code
COPY app.py .
COPY input/input.txt .

# Run the application
CMD ["python", "app.py"] 