FROM python:3.8-slim-buster

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
COPY .env .env

RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]