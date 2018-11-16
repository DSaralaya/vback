from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from app.main.util.serialize import serialize
import json

class users(declarative_base()):
     __tablename__ = 'users'

     Id=Column(Integer, primary_key=True,autoincrement=True)
     firstName=Column(String)
     lastName=Column(String)
     emailID=Column(String)
     mobileNo=Column(String)
     password=Column(String)


    
     

    