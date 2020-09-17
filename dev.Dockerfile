FROM python:3.7-alpine

COPY app/requirements.txt /

RUN pip install -r /requirements.txt
# --no-cache-dir

COPY app/ /app
WORKDIR /app

CMD ["env", "FLASK_APP=hello.py", "flask", "run", "--host", "0.0.0.0"]