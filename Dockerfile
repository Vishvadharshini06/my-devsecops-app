# Base Image
FROM python:3.9

# Set Working Directory
WORKDIR /bank

# Copy Code
COPY src/ .

# Run App
CMD ["python", "bank.py"]
