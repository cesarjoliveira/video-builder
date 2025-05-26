FROM python:3.13-slim

# Instala dependências de MoviePy e FFmpeg
RUN apt-get update && apt-get install -y ffmpeg libxext6 libxrender1 libglib2.0-0 libsm6 libx11-6
RUN apt-get update && apt-get install -y ffmpeg libxext6 libxrender1 libglib2.0-0 libsm6 libx11-6

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["runpod", "--handler", "main.handler"]
