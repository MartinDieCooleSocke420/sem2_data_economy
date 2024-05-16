FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and Python script
COPY requirements.txt .
COPY parking_simulator.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script
CMD ["python", "parking_simulator.py"]
