import json
from sqlalchemy import inspect

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
    for c in inspect(obj).mapper.column_attrs}



class parser(object):

     @classmethod
     def parseClass(self,schema,model):
        for item in model.keys():
            setattr(schema,item,model[item])
        return schema
 
     @classmethod
     def FromFile(clsself, filepath):
        result = None
        with open(filepath, 'r') as jfile:
            result = clsself.FromJSON(jfile.read())
        return result

     
     def convertJson(self):
        return json.dumps(self,default=object_as_dict)



   

   
     