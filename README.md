# 1-2-3-Heroku-Docker-Python-MongoDB

This is the sample app of the [1, 2, 3: Docker, Heroku, MongoDB Atlas, Python](https://beppecatanese.medium.com/1-2-3-docker-heroku-mongodb-atlas-python-952958423bea) tutorial.


 

## Setup

Clone the repository

```
git clone https://github.com/gcatanese/1-2-3-Heroku-Docker-Python-MongoDB.git
```

Create and *.env* file in the same folder as *app.py*. The *.env* file defines the environment variables:
```
MONGO_CONNECT_STRING=mongodb+srv://{db_username}:{db_password}@devcluster.s4lc7.mongodb.net/{db_name}?retryWrites=true&w=majority
``` 
Configure the placeholders accordingly:
* db_username: username of the MongoDB user
* db_password: password of the MongoDB user
* db_name: name of the MongoDB database

## Run 
Run the application
```
python app.py
```
