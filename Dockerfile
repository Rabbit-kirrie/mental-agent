FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=backend/app.py
CMD ["gunicorn","-w","4","-b","0.0.0.0:8000","backend.app:app"]
