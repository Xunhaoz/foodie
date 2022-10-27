FROM ubuntu:20.04

WORKDIR /foodie

ADD . /foodie

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install python3-pip -y
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt 

CMD ["python3", "app.py"]