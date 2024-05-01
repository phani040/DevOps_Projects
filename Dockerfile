#Base Image

FROM python:3.8

#set the working directory in the container

WORKDIR /app

#Copy the resquirements file

COPY requirements.txt .


#install the project dependecies

RUN pip install -r requirements.txt

#Copy the application code into the container

COPY . .

#Export the port that the flask application will be listening on

EXPOSE 5000

#Run the flask app

CMD ["python", "app.py"]
