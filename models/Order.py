from app import db
import unittest

class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(64))
    customer_phone = db.Column(db.Double)
    customer_address = db.Column(db.String(64))
    order_delivered = db.Column(db.Boolean,nullable=False, server_default="false") 
    order_item = db.relationship("Order_Item", backref="order")
    # items=db.relationship("Item", secondary='Order_item')

    def __repr__(self):
        return f'<Order "{self.customer_name}">' 
