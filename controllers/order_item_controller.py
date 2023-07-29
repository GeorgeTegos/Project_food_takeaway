from flask import flash,Blueprint,render_template,redirect,request
from app import db
# from models.Item import Item
# from models.Order import Order
from models.Order_item  import Order_Item


order_item_blueprint=Blueprint("order_item",__name__)

@order_item_blueprint.route('/test')
def test():
    order_list=Order_Item.query.all()
    return render_template('test.jinja',order_list=order_list)