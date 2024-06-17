FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY weather-collector.py .

CMD ["python", "weather-collector.py"]
