# Use full image with pip and venv
FROM python:3.11
    

# Install Node.js + npm
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Set working directory
WORKDIR /workspaces/order-book-engine

COPY . .

ENV PYTHONPATH=/workspaces/order-book-engine/src

# Copy requirements
COPY requirements.txt .

# Install Python packages
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

# Run app
CMD ["python3", "src/app.py"]
