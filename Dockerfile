# ビルド用のコンテナ

# FROM python:3.10.8-buster as builder
FROM python:3.10.8-buster

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# docker run -d --name mycontainer -p 80:80 testimage