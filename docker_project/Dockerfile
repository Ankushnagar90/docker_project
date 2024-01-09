FROM python:3-slim-buster

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app 

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# runs the production server
# ENTRYPOINT ["python", "mysite/manage.py"]
# CMD ["runserver", "0.0.0.0:8000"]

