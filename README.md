# API
1. Create virtual environment (inside selected folder):
    -sudo apt install python3.8-venv
    -python3 -m venv .venv
2. Activate virtual environment:
    -source .venv/bin/activate
    -to deactivate: deactivate
3. Install flask:
    -pip install flask
    -pip install flask-sqlalchemy
4. Create file to keep track of requirements:
    -pip freeze > requirements.txt
5. Create main file for the api:
    -touch application.py
6. After setting up Flask in main file and defining main endpoint, run the application (needs to be run everytime the venv is closed):
    -export FLASK_APP=application.py
    -export FLASK_ENV=development
    -flask run
    -ctrl+c quits flask app
7. After creating class to manage database, configuring database and creating class to definbe tables and columns, create database:
    -run python terminal: python3
    -from application import db
    -db.create_all()
8. Create database entries:
    -run python terminal: python
    -import Class needed: from application import Drink
    -drink = Drink(name="Soda", description="Tastes like grapes")
    -db.session.add(drink)
    -db.session.commit()
    -Query table: Drink.query.all()