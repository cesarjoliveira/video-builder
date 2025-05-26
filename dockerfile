FROM runpod/pytorch:3.10-py3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["runpod", "--handler", "main.handler"]
