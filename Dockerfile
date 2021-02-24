# set base image (host OS)
FROM python:3-alpine

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY pythonProject/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY pythonProject/ .

# commands to run on container start
CMD [ "python", "rest_app.py" ]