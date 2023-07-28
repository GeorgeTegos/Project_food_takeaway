from flask import flash,Blueprint,render_template,redirect,request
from app import db
from models.Item import Item
from models.Order import Order
from models.Order_item  import Order_Item


order_blueprint=Blueprint("order",__name__)

@order_blueprint.route('/orders')
def show_all_orders():
    orders = Order.query.all() 
    return render_template('orders/show.jinja',orders=orders)