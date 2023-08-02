from flask import flash,Blueprint,render_template,redirect,request
from app import db
from models.Item import Item
from models.Order import Order
from models.Order_item  import Order_Item


item_blueprint=Blueprint("item",__name__)

@item_blueprint.route('/items')
def show_all_items():
    items = Item.query.all()
    return render_template("items/items.jinja",items=items)


## TODO ###### Plus form
@item_blueprint.route('/item/<id>')
def show_specific_item(id):
    item = Item.query.get(id)
    return render_template("items/show_item.jinja",item=item)



@item_blueprint.route('/items/add')
def add_item_form():
    return render_template('items/new_item.jinja')

@item_blueprint.route('/items', methods=['POST'])
def add_new_item():
    item_name = request.form['item_name']
    item_price = request.form['item_price']
    new_item = Item(item_name=item_name, item_price=item_price)
    db.session.add(new_item)
    db.session.commit()
    return redirect('/items')




## TODO #######
@item_blueprint.route('/item/<id>/edit')
def edit_item(id):
    item = Item.query.get(id)
    return render_template('items/edit_item.jinja',item = item)

@item_blueprint.route('/item/<id>', methods=['post'])
def confirm_edit(id):
    item_name = request.form['item_name']
    item_price = request.form['item_price']
    edit_item = Item.query.get(id)
    edit_item.item_name = item_name
    edit_item.item_price = item_price
    db.session.commit()
    return redirect('/items')

@item_blueprint.route('/item/<id>/delete')
def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/items')