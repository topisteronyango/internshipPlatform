FROM python:3.10.12-slim

# Update apt-get cache and install required packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libcairo2-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt ./

# Install Python dependencies
RUN pip install -r requirements.txt --no-cache-dir \
    2>&1 | tee install.log

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["gunicorn", "InternBoard.wsgi:application", "--log-file", "-", "--log-level", "debug"]
