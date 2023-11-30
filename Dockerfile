FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the exam directory contents into the container at /app (see .dockerignore to check all ignored files)
COPY . /app

# Run pip to install requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python",  "main.py"]