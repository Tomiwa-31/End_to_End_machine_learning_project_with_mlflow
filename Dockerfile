FROM python:3.8-slim-buster

WORKDIR /app

# Copy everything first
COPY . .

# Then install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set Python path
ENV PYTHONPATH=/app/src

# Create necessary directories
RUN mkdir -p artifacts/data_ingestion \
    artifacts/data_validation \
    artifacts/data_transformation \
    artifacts/model_trainer \
    artifacts/model_evaluation \
    logs

EXPOSE 5000

CMD ["python", "app.py"]