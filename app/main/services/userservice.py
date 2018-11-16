from app.main.util.db import dbConnection
from app.main.models.usermodel import users
import json

class userservice:
   
    def __init__(self):
        self.connection=dbConnection()
    
    def getall(self):
        return self.connection.getall(users)

   
    def add(self,model):
        return self.connection.add(users,json.loads(model))
    
    def update(self,model):
        return self.connection.update(users,json.loads(model))


    