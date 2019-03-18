FROM python:3.7-alpine
MAINTAINER Claudio Yacarini <cyacarinic@gmail.com>

RUN mkdir /usr/local/opt
WORKDIR /usr/local/opt

# Install dependencies
RUN pip install --upgrade pip

# Install requirements
ADD ./code/requirements.txt /usr/local/opt/
RUN pip install -r requirements.txt

# Add Project
ADD ./code/ /usr/local/opt
