FROM python:3.9.0-alpine3.12

COPY requirements.txt .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

#COPY src/ .
CMD ["python", "./app.py"]

EXPOSE 5000