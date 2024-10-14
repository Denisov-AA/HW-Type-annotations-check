FROM python:3.13.0rc1-slim
WORKDIR /app
COPY . .
RUN pip install poetry pyright
RUN apt-get update && apt-get install make
