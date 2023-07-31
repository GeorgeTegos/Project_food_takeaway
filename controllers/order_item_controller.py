from flask import flash,Blueprint,render_template,redirect,request
from sqlalchemy import func
from app import db
from models.Item import Item
from models.Order import Order
from models.Order_item  import Order_Item


order_item_blueprint=Blueprint("order_item",__name__)

@order_item_blueprint.route('/ttest')
def test():
    order_list=Order_Item.query.all()
    return render_template('test.jinja',order_list=order_list)

@order_item_blueprint.route('/order/<id>/items', methods=['POST'])
def add_items_to_last_order(id):
    
    order = Order.query.get(id)

    for k,v in request.form.items():
        if v != '0':
            item_in_order = Order_Item(order_id=order.id,item_id=k,quantity=int(v))
            db.session.add(item_in_order)

    db.session.commit()
    return redirect("/orders")
   

@order_item_blueprint.route('/order/<id>/add_items')
def get_items_form(id):
    order = Order.query.get(id)
    items = Item.query.all()

    return render_template('/order_item/add_item.jinja',items=items,order=order)