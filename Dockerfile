FROM python:3.6.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/requirements
WORKDIR /code
COPY requirements_docker.txt /code/
RUN pip install -r requirements_docker.txt
COPY . /code/
WORKDIR /code/homebase
CMD ["python", "manage.py", "runserver", "--settings=homebase.settings-docker", "0.0.0.0:8003"]