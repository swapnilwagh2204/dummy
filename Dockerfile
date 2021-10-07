FROM python:3.6-slim
RUN mkdir /demo
WORKDIR /demo
ADD . /demo
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0:8000

# docker build . -t todoapp

# docker run -d -p 8000:8000 todoapp