import app

"""This area for Venus -- /car CRUD"""

"""This area for Richard -- /review CRUD"""
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

if __name__ == '__main__':
    app.app.run(debug=True)