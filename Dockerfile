# Does not support python 3.9 or above
FROM python:3.8-bullseye

WORKDIR /app

COPY requirements.txt ./

RUN export CFLAGS=-fcommon && \
    pip install -r requirements.txt

COPY . .

RUN pip install ./

