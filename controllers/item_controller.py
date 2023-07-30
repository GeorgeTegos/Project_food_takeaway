from flask import flash,Blueprint,render_template,redirect,request
from app import db
from models.Item import Item
from models.Order import Order
from models.Order_item  import Order_Item


item_blueprint=Blueprint("item",__name__)

@item_blueprint.route('/items')
def show_all_items():
    items = Item.query.all()
    return render_template("items/show.jinja",items=items)