FROM python:3.9.0-alpine3.12

COPY requirements.txt .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

#COPY src/ .
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]

EXPOSE 5000