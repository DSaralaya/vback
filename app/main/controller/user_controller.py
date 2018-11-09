from flask import  Blueprint,request,jsonify
user = Blueprint('user', __name__)

@user.route("/user", methods=['GET'])
def new_post():
    return 'new Posts'

@user.route("/user/add", methods=['POST'])
def add():
    t=request.get_json(silent=True);
    return  t['name']