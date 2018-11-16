import pymssql
from sqlalchemy import Table,create_engine,MetaData
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from app.main.util.parser import parser


class dbConnection(object):
    def __init__(self):
        connection_string = r"{0}://{1}:{2}@{3}/{4}".format(
            "mssql+pymssql", "admin",
            "oct@2018","LAP00021\SQLEXPRESS2014","vOffice")
        self.engine = create_engine(connection_string)
        
  
    def createSession(self):
        DBSession = sessionmaker(bind=self.engine)
        return DBSession()

    
    def getall(self,table):
      session= sessionmaker(bind=self.engine)()
      result = session.query(table).all()
      session.flush()
      return  result 

   
    def add(self,table,data):
      session= sessionmaker(bind=self.engine)()
      primary_key=str(table.metadata.sorted_tables[0].primary_key.columns.values()[0].name)
      Id=data[primary_key]
      del data[primary_key]
      model=parser.parseClass(table(),data)
      session.add(model)
      session.commit()
      return model 

   
    def update(self,table,model):
      session= sessionmaker(bind=self.engine)()
      primary_key=str(table.metadata.sorted_tables[0].primary_key.columns.values()[0].name)
      Id=model[primary_key]
      del model[primary_key]
      session.query(table).filter(getattr(table,primary_key)==Id).update(model)
      session.commit()
      return model

    