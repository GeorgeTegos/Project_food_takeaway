from app import db
from models.Item import Item
from models.Order import Order
from models.Order_item import Order_Item
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Order.query.delete()
    Item.query.delete()
    item1 = Item(item_name="Kebab",item_price=10)
    item2 = Item(item_name="Fish and Chips",item_price=15)
    item3 = Item(item_name="Club",item_price=7)

    order1 = Order(customer_name="George",customer_phone=1234567890,customer_address="Bon Gait",order_delivered=False)
    order2 = Order(customer_name="Nick",customer_phone=9809878987,customer_address="Princess Street",order_delivered=False)
    order3 = Order(customer_name="Bill",customer_phone=3241234123,customer_address="Princess Street North",order_delivered=False)


    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)

    db.session.commit()