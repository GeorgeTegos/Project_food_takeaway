from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/food_takeaway_project"
db=SQLAlchemy(app)
migrate=Migrate(app,db)

from controllers.item_controller import item_blueprint
from controllers.order_controller import order_blueprint
app.register_blueprint(item_blueprint)
app.register_blueprint(order_blueprint)

app.route('/')
def index():
    return render_template('index.jinja')