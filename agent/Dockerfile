# Use a lightweight Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the agent application code
COPY agent.py .

# Install any Python dependencies (none for this simple demo)
# RUN pip install requests # Example: if your agent needed HTTP requests

# Command to run the agent
CMD ["python", "agent.py"]
