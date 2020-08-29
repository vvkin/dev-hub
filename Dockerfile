# Base image
FROM python:3.8

# Enviroment variables for python executing
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Django for default works on localhost:8000
EXPOSE 8000

# Set working directory for backend (api)
WORKDIR /code/

# Copy pipenv files to docker container
COPY Pipfile Pipfile.lock /code/

# Install all dependencies from Pipfile.lock
RUN pip install pipenv && pip install Pillow && pipenv install --system

# All all code to docker container
COPY . /code/