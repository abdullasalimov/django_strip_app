FROM python:3.10.7-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
COPY .env /code/

RUN python3 -m pip install -r requirements.txt

COPY . /code/

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]