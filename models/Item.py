from app import db
import unittest

class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64))
    item_price = db.Column(db.Float)
    order_item = db.relationship("Order_Item", backref="item", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Item "{self.item_name}">' 
