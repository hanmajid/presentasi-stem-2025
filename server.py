from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__,
    static_folder='assets',
)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!</p>"