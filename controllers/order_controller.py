from flask import flash,Blueprint,render_template,redirect,request
from app import db
from models.Item import Item
from models.Order import Order
from models.Order_item  import Order_Item


order_blueprint=Blueprint("order",__name__)

@order_blueprint.route('/orders')
def show_all_orders():
    orders = Order.query.all()
    return render_template('orders/orders.jinja',orders=orders)

# @order_blueprint.route('/orders/<id>')
# def show_order_by_id(id):
#     order = Order.query.get(id)
#     phone= int(order.customer_phone)
#     return render_template("orders/show.jinja",order=order,phone=phone)

@order_blueprint.route('/orders/<id>')
def show_by_id(id):
    order = Order.query.get(id)
    items = Item.query.join(Order_Item).filter(Order_Item.order_id == id)
    total = 0
    for item in items:
        total += item.item_price
    return render_template('orders/show.jinja',order=order,items=items,total=total)