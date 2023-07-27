from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/food_takeaway_project"
db=SQLAlchemy(app)
migrate=Migrate(app,db)

from controllers.item_controller import item_blueprint
from controllers.order_controller import order_blueprint

