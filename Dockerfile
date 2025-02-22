FROM python:3.11

RUN mkdir /social

WORKDIR /social

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .