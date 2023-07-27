from app import db

class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(64))
    customer_phone = db.Column(db.Double)
    customer_address = db.Column(db.String(64))
    order_delivered = db.Column(db.Boolean, default = False)


class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64))
    item_price = db.Column(db.Integer)