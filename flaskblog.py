from app import create_app
from flask_cors import CORS
from flask import jsonify


app = create_app()
CORS(app)

@app.route('/')
def home():
    return jsonify('{ "connected":true}')

if __name__ == '__main__':
    app.run(debug=True)