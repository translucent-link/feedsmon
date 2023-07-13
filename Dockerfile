# Use an official Python runtime as the base image
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
  build-essential \
  flex \
  bison \
  libtool \
  make \
  automake \
  autoconf \
  build-essential \
  && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's source code
COPY . .

# Set any environment variables, if needed
EXPOSE 8000

# Specify the command to run your application
CMD [ "python", "main.py" ]