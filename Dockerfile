# Use full image with pip and venv
FROM python:3.11

# Set working directory
WORKDIR /src

# Copy requirements
COPY requirements.txt .

# Install Python packages
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

# Copy the rest of your app
COPY . .

# Run app
CMD ["python3", "src/app.py"]
