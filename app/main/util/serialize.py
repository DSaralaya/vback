import json

class serialize:
    def to_dict(model_instance, query_instance=None):
          if hasattr(model_instance, '__table__'):
               return {c.name: str(getattr(model_instance, c.name)) for c in model_instance.__table__.columns}
          else:
               cols = query_instance.column_descriptions
               return { cols[i]['name'] : model_instance[i]  for i in range(len(cols)) }
    
    
    def toJson(self):
        return json.dumps(self.to_dict())