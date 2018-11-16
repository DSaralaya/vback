import datetime
from functools import wraps
import jwt
from flask import Blueprint, jsonify, request

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['POST'])
def login():
    content = request.json
    if content and content['username'] == 'deepak@gmail.com' and content['password'] == 'sa123':
        auth_token = encode_auth_token('123')
        response_object = {
            'status': 'success',
            'message': 'Successfully logged in.',
            'Authorization': str(auth_token)
        }
        return jsonify(response_object), 200

    else:
        response_object = {
            'status': 'fail',
            'message': 'username or password does not match.'
        }
        return jsonify(response_object), 401


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = decode_auth_token(token)
            current_user = '123'
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(*args, **kwargs)

    return decorated


def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id,
            'role':'admin'
        }
        token = jwt.encode(payload, '1234', algorithm='HS256').decode('utf-8')
        return token
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, '1234', algorithm='HS256')
        if payload:
            return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
