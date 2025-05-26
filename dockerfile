FROM python:3.10-slim

WORKDIR /app

RUN pip install torch torchvision torchaudio && apt-get update && apt-get install -y ffmpeg

COPY . .

CMD ["runpod", "--handler", "main.handler"]
