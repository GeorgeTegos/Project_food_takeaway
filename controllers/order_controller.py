from flask import flash,Blueprint,render_template,redirect,request
from app import db
from models.Item import Item
from models.Order import Order
from models.Order_item  import Order_Item


order_blueprint=Blueprint("order",__name__)

@order_blueprint.route('/orders')
def show_all_orders():
    from sqlalchemy import desc
    orders = Order.query.order_by(desc(Order.id)).all()
    return render_template('orders/orders.jinja',orders=orders)


@order_blueprint.route('/order/find', methods=["post"])
def search_order_by_id():
    search = request.form['search']
    if len(search) == 0:
        return redirect('/orders')
    order = Order.query.get(int(search))
    if order ==  None:
        return redirect('/orders')
    phone = int(order.customer_phone)
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
    return redirect('/orders')


@order_blueprint.route('/order/<id>')
def show_by_id(id):
    order = Order.query.get(id)
    ordered_items = {}
    total = 0
    for item in order.order_item:
        ordered_items[item.item.item_name] = item.quantity      
        total += (item.item.item_price  * item.quantity)
    phone= int(order.customer_phone)
    return render_template('orders/show.jinja',order=order,total=total,phone=phone,ordered_items=ordered_items)

@order_blueprint.route('/order/<id>/edit_quantity')
def edit_item_quantity(id):
    order = Order.query.get(id)
    ordered_items = {}
    total = 0
    for item in order.order_item:
        ordered_items[item.item.item_name] = item.quantity      
        total += (item.item.item_price  * item.quantity)
    phone= int(order.customer_phone)
    return render_template('orders/edit_quantity.jinja',
                           order=order,total=total,phone=phone,ordered_items=ordered_items)


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
    phone= int(order.customer_phone)
    for item in order.order_item:
        print(item.item_id)
    
    return render_template('orders/edit.jinja',order=order,phone=phone,items=order.order_item)

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



@order_blueprint.route('/order/<id>/new_quantity', methods=['post'])
def confirm_new_quantity(id):
    order=Order.query.get(id)
    ordered_items = request.form.items()

    for k,v in ordered_items:
        if v != '0':
            item = Item.query.filter_by(item_name=k).first()
            order_item = Order_Item.query.filter_by(item_id=item.id, order_id=order.id).first()
            order_item.quantity = v
        elif v == '0':
            item = Item.query.filter_by(item_name=k).first()
            order_item = Order_Item.query.filter_by(item_id=item.id, order_id=order.id).first()
            db.session.delete(order_item)

    db.session.commit()
    return redirect('/orders')


@order_blueprint.route('/orders/<id>/button', methods=['post'])
def update_status_button(id):
    order = Order.query.get(id)
    try:
        request.form["delivered"]
        delivered=True
    except KeyError:
        delivered=False
    order.order_delivered=delivered
    db.session.commit()
    return redirect('/orders')

####################

