import app

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
    result = reviews_schema.dump(all_products) # dump is part of Marshmallow

    return jsonify(result.data)

# Retrieve (GET) single review
@app.route('/reviews/<id>', methods=['GET'])
def get_review(id):
    review = Review.query.get(id)

    return review_schema.jsonify(product)

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

    return review_schema.jsonify(product)

# Delete review
@app.route('/reviews/<id>', methods=['DELETE'])
def delete_product(id):
    review = Review.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return review_schema.jsonify(product)
#Create API Route for Creating Cars
@app.route('/Cars',methods=['POST'])
def add_product():
    make = request.json['make']
    model = request.json['model']
    price = request.json['price']
    body_type = request.json['body_type']
    color = request.json['color']
    image = request.json['image']
    mileage = request.json['mileage']

    #init cars with info
    new_car = Product(make,model,price,body_type,color,image,mileage)

    db.session.add(new_car)
    db.session.commit()

    return cars_schema.jsonify(new_car)

#GET All Cars
@app.route('/Cars',methods=["GET"])
def get_products():
    all_cars = Cars.query.all()
    result = cars_schema.dump(new_car)
    return jsonify(result.data)

#GET Single Car
@app.route('/Cars/<id>',methods=["GET"])
def get_product(id):
    cars = Cars.query.get(id)
    return cars_schema.jsonify(cars)

#Update Cars
@app.route('/product/<id>',methods=["PUT"])
def update_product(id):
    cars = Cars.query.get(id)

    make = request.json['make']
    model = request.json['model']
    price = request.json['price']
    body_type = request.json['body_type']
    color = request.json['color']
    image = request.json['image']
    mileage = request.json['mileage']

    cars.make = make
    cars.model = model
    cars.price = price
    cars.body_type = body_type
    cars.color = color
    cars.image = image
    cars.mileage = mileage

    db.session.commit()

    return cars_schema.jsonify(cars)

#Delete Cars
@app.route('/Cars/<id>',methods=["DELETE"])
def delete_product(id):
    cars = Cars.query.get(id)
    db.session.delete(cars)
    db.session.commit()

    return cars_schema.jsonify(cars)


if __name__ == '__main__':
    app.app.run(debug=True)