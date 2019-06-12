from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from app import app

# Init App

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__)) #Considers your OS and finds the base path so it can work across machines

# Database Config

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://akbkozrj:XgCf78t_z7wqYBT-xSQtldUvlVz0opRq@otto.db.elephantsql.com:5432/akbkozrj" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize our Database

db = SQLAlchemy(app)

# Init Marshmallow

ma = Marshmallow(app)

# Create Car Model

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100))
    model = db.Column(db.String(200))
    price = db.Column(db.Float)
    body_type = db.Column(db.String(100))
    color = db.Column(db.String(100))
    image = db.Column(db.String(100))
    mileage = db.Column(db.Integer)

    def __init__(self,make,model,price,body_type,color,image,mileage): # Every product needs to be initialized with these set parameters - id will auto-assign
        self.make = make
        self.model = model
        self.price = price
        self.body_type = body_type
        self.color = color
        self.image = image
        self.mileage = mileage

    def __repr__(self):
        return '<Car {}>'.format(self.make)

class CarSchema(ma.Schema): # ma is Marshmallow instantiation as seen above
    class Meta:
        fields = ('id', 'make', 'model', 'price', 'body_type','color','image','mileage') # fields is a property of Schema 

# Init Schema

car_schema = CarSchema(strict=True) # strict = True is to avoid warnings in console
cars_schema = CarSchema(many=True,strict=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    message = db.Column(db.String(250))

    def __init__(self,name,rating,message):
        self.name = name
        self.rating = rating
        self.message = message


class ReviewSchema(ma.Schema): # ma is Marshmallow instantiation as seen above
    class Meta:
        fields = ('id', 'name', 'rating', 'message') # fields is a property of Schema 

review_schema = ReviewSchema(strict=True) # strict = True is to avoid warnings in console
reviews_schema = ReviewSchema(many=True,strict=True)

#TODO run db.create_all() in python shell (from models import db)

