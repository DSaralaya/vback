from flask import  Blueprint,request,jsonify
from app.main.util.auth import token_required
from app.main.services.userservice import userservice
from app.main.util.parser import object_as_dict
import json

user = Blueprint('user', __name__)


@user.route("/user", methods=['GET'])
def getall():
     result= userservice().getall()
     return json.dumps(result, default=object_as_dict)

@user.route("/user", methods=['POST'])
def add():
    data=json.dumps(request.get_json(silent=True))
    result= userservice().add(data)
    return json.dumps(result, default=object_as_dict)

@user.route("/user", methods=['PUT'])
def update():
    data=json.dumps(request.get_json(silent=True))
    result= userservice().update(data)
    return json.dumps(result, default=object_as_dict)

   