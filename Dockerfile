FROM python:3.8.5
ADD . /api
WORKDIR /api
RUN pip install -r requirements.txt
