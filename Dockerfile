FROM python:3.13-alpine

RUN apk --no-cache add curl

RUN pip install --no-cache-dir flask

COPY app.py /app.py

EXPOSE 8080

CMD ["python", "/app.py"]
