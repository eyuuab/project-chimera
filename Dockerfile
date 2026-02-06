# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

# Set work directory
WORKDIR /app

# Install system dependencies (curl is needed for healthchecks/tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv (The Python Package Manager)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency definitions first (Layer Caching)
COPY pyproject.toml uv.lock ./

# Sync dependencies (This installs everything in pyproject.toml)
RUN uv sync --frozen

# Copy the rest of the application code
COPY . .

# Default command: Run the tests
CMD ["uv", "run", "pytest", "tests/"]