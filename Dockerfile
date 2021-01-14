FROM python:3.9.0a5-alpine3.10
RUN mkdir /code
COPY . /code/
WORKDIR /code/
RUN pip freeze > requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt