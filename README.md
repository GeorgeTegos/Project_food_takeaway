This is my first solo project, a food take-away web app for employees taking orders.
For this project I used: Python, HTML, CSS, Flask, SQLAlchemy.
Duration of the project was 1 week.

You can see a 3minutes showcase by download food_take_away_showcase file.

If you want to use this web app. 
1)You need Flask - SQLalchemy

2)You have to change from app.py this line :
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/food_takeaway_project"
by replacing:
user@localhost:5432    to  YOUR_USER_NAME@localhost:5432

3)use this command to create local database (MAC):createdb food_takeaway_project 
into the folder use those commands in that order:
  flask db init
  flask db migrate
  flask db upgrade

4) use this command to run flask: flask run

5) Flask enviroment runs at port 4999 so you can go to web app homepage by typing this URL: http://localhost:4999/
