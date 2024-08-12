FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install flask flasgger

CMD ["python", "app.py"]
