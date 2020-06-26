FROM python:3.6.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/requirements
WORKDIR /code
COPY requirements_docker.txt /code/
RUN pip install -r requirements_docker.txt
COPY . /code/
WORKDIR /code/homebase
CMD ["python", "manage.py", "runserver", "--settings=homebase.settings-docker", "0.0.0.0:8000"]

# build the image
# sudo docker build -t my_homebase:latest .

# run the container
# cd ~/shared (make sure that homebase.sqlite3 is here)
# sudo docker run --name my_homebase --mount type=bind,source="$(pwd)",target=/shared -p 8003:8000 --restart always my_homebase:latest &
