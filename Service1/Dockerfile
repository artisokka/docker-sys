FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y procps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir docker
COPY . .
EXPOSE 8199
CMD ["python", "app.py"]
