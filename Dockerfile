FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create required directories
RUN mkdir -p output input

# Copy the application code
COPY app.py .
# (Optional) You can mount ./input via docker-compose; no default file copied
COPY templates/ ./templates/

# Expose web port
ENV PORT=8000
EXPOSE 8000

# Run the application (Flask dev server is fine for this small tool)
CMD ["python", "app.py"] 