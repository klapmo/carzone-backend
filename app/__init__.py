from flask import Flask

from flask_cors import CORS
app = Flask(__name__)

cors = CORS(app,resources = {"/cars":{"origins":"*"}})
cors = CORS(app,resources = {"/reviews": {"origins":"*"}})