# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /src

# Create and activate a virtual environment
RUN python -m venv /venv

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip3.11 install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . .

# Default command: run the script (can be overridden)
CMD ["python", "src/app.py"]
