from app import db
import unittest

class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64))
    item_price = db.Column(db.Integer)
    order_item = db.relationship("Order_Item", backref="item")
