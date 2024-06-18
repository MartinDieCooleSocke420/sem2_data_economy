FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY parking_simulation.py .

CMD ["python", "parking_simulation.py"]
