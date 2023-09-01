FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip \
        && pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]