# Week 1 — App Containerization

## Containerize Application 

### Add Dockerfile for Backend: [Backend Dockerfile](/backend-flask/Dockerfile)

![Image of Backend Dockerfile](assets/backend-dockerfile.png)


## Document the Notification Endpoint for the OpenAI Document

![Documentation OpenAI Endpoint](assets/open-ai.png)


## Write a Flask Backend Endpoint for Notifications

Code found [here](/backend-flask/app.py)

![Backend Endpoint for Notifications](assets/backend.png)


## Write a React Page for Notifications

Code found [here](/frontend-react-js/src/pages/NotificationsFeedPage.js)

![React Pagefeed for Notifications](assets/react.png)

## Run DynamoDB Local Container and ensure it works

Create a table from example found [here](https://github.com/100DaysOfCloud/challenge-dynamodb-local)

![React Pagefeed for Notifications](assets/dynamodb-table.png)

## Run Postgres Container and ensure it works

From terminal, run the command: 
```
psql -h localhost -U postgres
```

![React Pagefeed for Notifications](assets/postgres.png)

## Stretch Assignments

### Push and tag an image to Docker Hub

As a stretch assignment, I pushed and tagged an image to Docker Hub found [here](https://hub.docker.com/repository/docker/amehi4yus/reactquiz/general)

![Docker Hub Image](assets/dockerhub.png)

### Learn how to install Docker on your local machine and run the containers
- Download, install and run Docker Desktop : https://hub.docker.com/
	![Image of Docker Desktop](assets/docker-desktop.png)
- Download zip file found [here](https://github.com/amehi0index/aws-bootcamp-cruddr-2023)
- Delete meta.json file from path as explained [here](https://stackoverflow.com/questions/74804296/docker-endpoint-for-default-not-found) 
	
- In the terminal, change directories into fontend-react-js directory:
	```
	 cd frontend-react-js
	```
   From the frontend-react-js directory, run the command:
   
	 ```
	 npm install
	 ```
- Right click on docker-compose.yml file located in the Explorer panel, select Compose Up to run containers locally in VSCode editor
	![Image from local VS Code Terminal](assets/local-docker.png)


