# Config
FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /

COPY requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt

COPY . /

ARG SECRET_KEY
ARG DEBUG
ARG SENTRY_DSN

RUN python manage.py collectstatic --noinput --clear

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
