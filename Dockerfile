FROM python:3.10-slim-bullseye
RUN apt-get update && apt-get install --no-install-recommends -y bash nano mc
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src
COPY . /src/
RUN pip install -r requirements/prod.txt
WORKDIR /src/homebase
RUN exec python manage.py collectstatic --settings=homebase.settings.docker --no-input
CMD exec gunicorn homebase.wsgi_docker:application --bind 0.0.0.0:8000 --workers 3

# build the image
# docker build -t my_homebase:latest .

# run the container
# cd ~/shared (make sure that homebase.sqlite3 is here)
# docker run -d --name my_homebase --mount type=bind,source=$HOME/shared,target=/shared -p 8003:8000 --restart always my_homebase:latest &
