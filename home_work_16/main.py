from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import utills

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///informations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    role = db.Column(db.String)
    phone = db.Column(db.String)

    def user_data_json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    customer = db.relationship("User", foreign_keys=[customer_id])
    executor = db.relationship("User", foreign_keys=[executor_id])

    def order_data_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    order = db.relationship("Order", foreign_keys=[order_id])
    executor = db.relationship("User", foreign_keys=[executor_id])

    def offer_data_json(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }


with app.app_context():
    db.create_all()

db.session.add_all(utills.con_tab_user(User))
db.session.commit()

db.session.add_all(utills.con_tab_order(Order))
db.session.commit()

db.session.add_all(utills.con_tab_offer(Offer))
db.session.commit()


@app.route("/users", methods=['GET', 'POST'])
def get_all_users():
    if request.method == "GET":
        result = []
        for user in User.query.all():
            result.append(User.user_data_json(user))
        return jsonify(result)

    elif request.method == "POST":
        inf_user = json.loads(request.data)
        add_user = utills.add_user_json(inf_user, User)
        db.session.add(add_user)
        db.session.commit()
        return jsonify(User.user_data_json(add_user))


@app.route("/users/<int:pk>", methods=['GET', 'PUT', 'DELETE'])
def get_user(pk):
    if request.method == "GET":
        result = User.query.get(pk)
        return jsonify(User.user_data_json(result))

    elif request.method == 'PUT':
        new_inform = request.json
        result = User.query.get(pk)
        result.first_name = new_inform.get("first_name")
        result.last_name = new_inform.get("last_name")
        result.age = new_inform.get("age")
        result.email = new_inform.get("email")
        result.role = new_inform.get("role")
        result.phone = new_inform.get("phone")
        db.session.add(result)
        db.session.commit()
        return f"Обновление User {pk} успешно\n {jsonify(new_inform)}"

    elif request.method == 'DELETE':
        result = User.query.get(pk)
        db.session.delete(result)
        db.session.commit()
        return f"User {pk} успешно удалён"


@app.route("/orders", methods=['GET', 'POST'])
def get_all_orders():
    if request.method == "GET":
        result = []
        for order in Order.query.all():
            result.append(Order.order_data_json(order))
        return jsonify(result)

    elif request.method == "POST":
        inf_order = json.loads(request.data)
        add_order = utills.add_order_json(inf_order, Order)
        db.session.add(add_order)
        db.session.commit()
        return jsonify(Order.order_data_json(add_order))


@app.route("/orders/<int:pk>", methods=['GET', 'PUT', 'DELETE'])
def get_order(pk):
    if request.method == "GET":
        result = Order.query.get(pk)
        return jsonify(Order.order_data_json(result))

    elif request.method == "PUT":
        new_inform = request.json
        result = Order.query.get(pk)
        result.name = new_inform.get("name")
        result.description = new_inform.get("description")
        result.start_date = new_inform.get("start_date")
        result.end_date = new_inform.get("end_date")
        result.address = new_inform.get("address")
        result.price = new_inform.get("price")
        result.customer_id = new_inform.get("customer_id")
        result.executor_id = new_inform.get("executor_id")
        db.session.add(result)
        db.session.commit()
        return f"Обновление Order {pk} успешно\n {jsonify(new_inform)}"

    elif request.method == "DELETE":
        result = Order.query.get(pk)
        db.session.delete(result)
        db.session.commit()
        return f"Order {pk} успешно удалён"


@app.route("/offers", methods=['GET', 'POST'])
def offers():
    if request.method == "GET":
        result = []
        for offer in Offer.query.all():
            result.append(Offer.offer_data_json(offer))
        return jsonify(result)

    elif request.method == "POST":
        inf_offer = json.loads(request.data)
        add_offer = utills.add_offer_json(inf_offer, Offer)
        db.session.add(add_offer)
        db.session.commit()
        return jsonify(Offer.offer_data_json(add_offer))


@app.route("/offers/<int:pk>", methods=['GET', 'PUT', 'DELETE'])
def get_offer(pk):
    if request.method == "GET":
        result = Offer.query.get(pk)
        return jsonify(Offer.offer_data_json(result))

    elif request.method == "PUT":
        new_inform = request.json
        result = Offer.query.get(pk)
        result.order_id = new_inform.get("order_id")
        result.executor_id = new_inform.get("executor_id")
        db.session.add(result)
        db.session.commit()
        return f"Обновление Offer {pk} успешно\n {jsonify(new_inform)}"

    elif request.method == 'DELETE':
        result = Offer.query.get(pk)
        db.session.delete(result)
        db.session.commit()
        return f"Offer {pk} успешно удалён"


@app.errorhandler(404)
def page_not_found(e):
    return f"Упс произошла ошибка 404"


# Обработка ошибки 500
@app.errorhandler(500)
def page_not_found(e):
    return f"Упс произошла ошибка 500"


if __name__ == "__main__":
    app.run(debug=True)
