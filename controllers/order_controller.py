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


@order_blueprint.route('/order/find', methods=["post"])
def search_order_by_id():
    search = request.form['search']
    print(type(search))
    order = Order.query.get(int(search))
    phone = int(order.customer_phone)
    # total = find_total(order.order_item)
    ordered_items = {}
    total = 0
    for item in order.order_item:
        ordered_items[item.item.item_name] = item.quantity      
        total += (item.item.item_price  * item.quantity) 
    return render_template('orders/show.jinja',order=order,total = total,phone=phone, ordered_items=ordered_items)


@order_blueprint.route('/order/<id>/delete')
def delete_order(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()
    return redirect('/')


@order_blueprint.route('/order/<id>')
def show_by_id(id):
    order = Order.query.get(id)
    # total = find_total(order.order_item)
    ordered_items = {}
    total = 0
    for item in order.order_item:
        ordered_items[item.item.item_name] = item.quantity      
        total += (item.item.item_price  * item.quantity)
    phone= int(order.customer_phone)

    return render_template('orders/show.jinja',order=order,total=total,phone=phone,ordered_items=ordered_items)

@order_blueprint.route('/orders/new')
def make_new_order_form():
    items = Item.query.all()
    return render_template('orders/new_order.jinja',items=items)

@order_blueprint.route('/orders', methods=['POST'])
def make_new_order():
    name = request.form['customer_name']
    phone = request.form['customer_phone']
    address = request.form['customer_address']
    new_order = Order(customer_name=name, customer_phone=phone, customer_address=address)
    db.session.add(new_order)
    db.session.commit()
    return redirect('/orders')

@order_blueprint.route('/orders/<id>/edit')
def edit_order(id):
    order = Order.query.get(id)
    items = Item.query.join(Order_Item).filter(Order_Item.order_id == id)
    phone= int(order.customer_phone)
    
    return render_template('orders/edit.jinja',order=order,items=items,phone=phone)

@order_blueprint.route("/orders/<id>" , methods=["post"])
def confirm_edit(id):

    name = request.form['customer_name']
    phone = request.form['customer_phone']
    address = request.form['customer_address']
    order = Order.query.get(id)

    order.customer_name = name
    order.customer_phone = phone
    order.customer_address = address
    try:
        request.form["delivered"]
        delivered=True
    except KeyError:
        delivered=False
    order.order_delivered=delivered


    db.session.commit()
    return redirect('/orders')

####################

def find_total(dictionary):
    ordered_items = {}
    total = 0
    for item in dictionary:
        ordered_items[item.item.item_name] = item.quantity      
        total += (item.item.item_price  * item.quantity) 
    return total