FROM python:3.9-bullseye
EXPOSE 5000
WORKDIR /ValueWIneBack/
COPY requirements.txt /ValueWIneBack/
RUN python -m pip install -U pip
RUN pip install -r requirements.txt
COPY . /ValueWIneBack/
WORKDIR /ValueWIneBack/
ENV FLASK_APP=/ValueWIneBack/__init__.py
CMD flask run --host=0.0.0.0
