import os

from apig_wsgi import make_lambda_handler
from flask import Flask


# Flask app
app = Flask(__name__)


@app.route("/")
def index():
    return '<b>AWS serverless sample</b>'


@app.route("/hello")
def hello_world():
    return '<p>Hello, World!</p>'


# Configure this as your entry point in AWS Lambda
_lambda_handler = make_lambda_handler(app)


def lambda_handler(event, context):
    # noinspection PyCallingNonCallable
    return _lambda_handler(event, context)


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = os.environ.get('ALLOW_ORIGIN')
    return response
