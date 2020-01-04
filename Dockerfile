FROM ubuntu:latest
MAINTAINER Dibyendu Biswas
WORKDIR /Docker_App
COPY src/requirements.txt ./
ADD Python-3.6.10.tgz /Docker_App
RUN apt-get update && apt-get install -y python-pip
RUN pip install --requirement requirements.txt
COPY src /Docker_App
EXPOSE 80
ENTRYPOINT [ “python” ]
CMD [ "app.py" ]
