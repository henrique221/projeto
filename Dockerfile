FROM python:3.6-onbuild

RUN mkdir -p /projeto1

WORKDIR /projeto1

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY . .

EXPOSE 5000
