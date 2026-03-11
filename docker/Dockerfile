# Stage 1: Build
FROM python:3.11-slim AS builder

WORKDIR /app

# Create a non-root user
RUN useradd -m appuser

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY backend/ .

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Copy the installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app /app

# Switch to non-root user
USER appuser

# Expose the API port
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]