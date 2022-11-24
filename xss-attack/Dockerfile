FROM php:7.1.2-apache 
RUN docker-php-ext-install mysqli pdo pdo_mysql
FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install flask
CMD python app.py
