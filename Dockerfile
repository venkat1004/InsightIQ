# Use a specific version of Python (>=3.10)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the project directory (where Dockerfile is located) into the container
COPY . /app

# Install any required packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit runs on (default: 8501)
EXPOSE 8501

# Run Streamlit app (change to app.py)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
