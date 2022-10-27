FROM ubuntu:18.04

WORKDIR /foodie

ADD . /foodie/

RUN sudo apt-get update -y
RUN sudo apt-get install -y python3
RUN pip install -r requirements.txt 

CMD ["python3", "app.py"]