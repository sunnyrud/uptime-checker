FROM python:3.11-slim

WORKDIR /app

COPY uptime-checker.py .

RUN pip install requests

CMD ["python", "uptime-checker.py"]
