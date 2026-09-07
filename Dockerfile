FROM python:3.9-slim

WORKDIR /app

COPY backend/requirement.txt .

RUN pip install -r requirements.txt

COPY backend/app.py .

EXPOSE 5000

CMD["python","app.py"]