import app

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