FROM python:3.6
ADD . /usr/src/app
RUN pip install -r /usr/src/app/docs/requeriments.txt
