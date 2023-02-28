#Get Python image from DockerHub
FROM python:3.10-slim-buster

#Set working directory within container
WORKDIR /backend-flask

#Outside container(src) -> inside container(dest)
#contains libs to install to run the app
COPY requirements.txt requirements.txt

#Inside container
#Install Python libs used for the app
#RUN creates layer in image
RUN pip3 install -r requirements.txt

#Outside(src) -> inside(dest)
# . --> means verything in the current directory
COPY . .

#Set env vars inside container
ENV FLASK_ENV=development

EXPOSE ${PORT}

#Cmd to run flask when container starts up
#flask--> python -m flask run --host=0.0.0.0 --port=4567 
# -m = module / --host=0.0.0.0 = "everything" host
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
