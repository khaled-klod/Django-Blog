FROM python:3.6.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD ./ /code/
CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8001"]