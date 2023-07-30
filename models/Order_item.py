from app import db
import unittest

class Order_Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer,db.ForeignKey("order.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))

    def __repr__(self):
        return f'<Order_Item "{self.id}">' 