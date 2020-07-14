#
# Author: unb1cob
# Created: 15.Apr.2020

FROM ubuntu:latest

LABEL Name="AUNet servr"
LABEL Description="This image is to start aunet server which detects aunets from video"

# Install python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy source files of the auner server
COPY requirements.txt /home/base/requirements.txt

WORKDIR /home/base
RUN pip3 install -r requirements.txt

COPY server.py /home/base/server.py

# Add entry point
ENTRYPOINT [ "python3", "server.py"]

EXPOSE 11000
