# ビルド用のコンテナ

FROM python:3.10.8-buster as builder

WORKDIR /opt/app

COPY requirements.txt /opt/app

RUN pip3 install -r requirements.txt

# 実行用コンテナ
FROM python:3.10.8-slim-buster as runner

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

RUN apt-get update 
# && apt install -y uvicorn
#  && apt-get install -y %%%%% \
#  && apt-get clean 
#  && rm -rf /var/lib/apt/lists/*\

RUN cp -p /usr/share/zoneinfo/Japan /etc/localtime

RUN pip install setuptools

COPY . /opt/app/amazon-assistant-api

WORKDIR /opt/app/amazon-assistant-api

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]