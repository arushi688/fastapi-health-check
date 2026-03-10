FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Environment argument
ARG ENVIRONMENT

# Copy environment-specific file
COPY env/${ENVIRONMENT}.env .env

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]