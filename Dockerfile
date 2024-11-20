# Use the official Python base image from the Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container's working directory
COPY cricket_score_tracker.py .

# Install any dependencies if needed (none for this program)
# RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script
CMD ["python", "cricket_score_tracker.py"]
