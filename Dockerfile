FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /volume-data
RUN cp -r /app/. /volume-data/
CMD ["python", "main.py"]

