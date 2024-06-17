FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY weather_collector.py .

CMD ["python", "weather_collector.py"]
