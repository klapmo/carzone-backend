from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)
# TODO Add input for routes and models when models is created