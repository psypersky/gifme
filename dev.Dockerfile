FROM python:3.7-alpine

WORKDIR /gifme

COPY requirements.txt .

RUN pip install -r requirements.txt
# --no-cache-dir

COPY . .

ENV FLASK_ENV development

CMD ["python3", "server.py"]
