from app import app
from flask import Flask, request, jsonify
from models import Car,Review,db,cars_schema,car_schema,review_schema,reviews_schema


app = Flask(__name__)
# Create API route for creating product
# Create Review
@app.route('/reviews', methods=['POST'])
def addReview():
    name = request.json['name']
    rating = request.json['rating']
    message = request.json['message']

    # Initialize review with info
    new_review = Review(name, rating, message)

    db.session.add(new_review) # open the session
    db.session.commit() 

    return review_schema.jsonify(new_review)

# Retrieve (GET) all reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    all_reviews = Review.query.all()
    result = reviews_schema.dump(all_reviews) # dump is part of Marshmallow
    return jsonify(result.data)

# Retrieve (GET) single review
@app.route('/reviews/<id>', methods=['GET'])
def get_review(id):
    review = Review.query.get(id)
    return review_schema.jsonify(review)

# Update a review (inside of our database)
@app.route('/reviews/<id>', methods=['PUT'])
def update_review(id):
    review = Review.query.get(id)

    name = request.json['name']
    rating = request.json['rating']
    message = request.json['message']

    review.name = name
    review.rating = rating
    review.message = message

    db.session.commit()

    return review_schema.jsonify(review)

# Delete review
@app.route('/reviews/<id>', methods=['DELETE'])
def delete_product(id):
    review = Review.query.get(id)

    db.session.delete(review)
    db.session.commit()

    return review_schema.jsonify(review)
#Create API Route for Creating Cars
@app.route('/cars',methods=['POST'])
def add_car():
    make = request.json['make']
    model = request.json['model']
    price = request.json['price']
    body_type = request.json['body_type']
    color = request.json['color']
    image = request.json['image']
    mileage = request.json['mileage']

    #init cars with info
    new_car = Car(make,model,price,body_type,color,image,mileage)

    db.session.add(new_car)
    db.session.commit()

    return car_schema.jsonify(new_car)

#GET All Cars
@app.route('/cars',methods=["GET"])
def get_cars():
    all_cars = Car.query.all()
    result = cars_schema.dump(all_cars)
    return jsonify(result.data)

#GET Single Car
@app.route('/cars/<id>',methods=["GET"])
def get_car(id):
    car = Car.query.get(id)
    return car_schema.jsonify(cars)

#Update a Car
@app.route('/cars/<id>',methods=["PUT"])
def update_car(id):
    car = Car.query.get(id)

    make = request.json['make']
    model = request.json['model']
    price = request.json['price']
    body_type = request.json['body_type']
    color = request.json['color']
    image = request.json['image']
    mileage = request.json['mileage']

    car.make = make
    car.model = model
    car.price = price
    car.body_type = body_type
    car.color = color
    car.image = image
    car.mileage = mileage

    db.session.commit()

    return car_schema.jsonify(car)

#Delete Cars
@app.route('/cars/<id>',methods=["DELETE"])
def delete_car(id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    return car_schema.jsonify(car)


if __name__ == '__main__':
    app.run(debug=True)