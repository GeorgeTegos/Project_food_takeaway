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

@order_blueprint.route('/orders/<id>')
def show_by_id(id):
    order = Order.query.get(id)
    items = Item.query.join(Order_Item).filter(Order_Item.order_id == id)
    phone= int(order.customer_phone)
    total = 0
    for item in items:
        total += item.item_price
    return render_template('orders/show.jinja',order=order,items=items,total=total,phone=phone)

@order_blueprint.route('/orders/new')
def make_new_order():
    items = Item.query.all()
    return render_template('orders/new_order.jinja',items=items)

@order_blueprint.route('/orders', methods=['POST'])
def send_new_order():
    name = request.form['customer_name']
    phone = request.form['customer_phone']
    address = request.form['customer_address']

    new_order = Order(customer_name=name, customer_phone=phone, customer_address=address)


    db.session.add(new_order)
    db.session.commit()
    return redirect('/')