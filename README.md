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
7. After configuring database and creating class to define tables and columns, create database:
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


# Deploying on Heroku
reference 1: https://devcenter.heroku.com/articles/getting-started-with-python
reference 2:https://devcenter.heroku.com/articles/flask-memcache
1. Install Heroku (if needed)
    -sudo snap install heroku --classic
2. Login to Heroku
    -heroku login
3. Clone repository and navigate to its directory
    -git clone https://github.com/heroku/python-getting-started.git
    -cd python-getting-started
4. Create runtime.txt an requirements.txt files
    -touch runtime.txt
    -pip freeze > requirements.txt
5. Create and deploy app
    -heroku create
    -git push heroku main
6. Check if at least one instance of app is running
    -heroku ps:scale web=1
7. Open website
    -heroku open
8. View logs
    -heroku logs --tail
9. Define a Procfile
    -reference: https://devcenter.heroku.com/articles/procfile
10. Check number of dynos and scale app if needed
    -heroku ps
    -heroku ps:scale web=1 (number of dynos)
    -reference: https://devcenter.heroku.com/articles/dynos
11. Run app locally (for testing and debugging)
    -postgresql must be installed:
        -sudo apt install libpq-dev
        -sudo apt install postgresql
    -pip install -r requirements.txt
12. Run the app locally
    -python manage.py collectstatic (for Django apps)
    -heroku local web
13. Push local changes
    # 13.1 make any changes needed to the app then run locally
    -heroku local
    # 13.2 Deploy to Heroku
    -git add .
    -git commit -m "commit"
    -git push heroku main
    -heroku open
14. Provision add-ons (Papertrail example)
    -heroku addons:create papertrail (create add-on)
    -heroku addons (list add-ons)
    -heroku addons:open papertrail (view specific add-on)
15. Set config vars
    -heroku config:set TIMES=2 (set configuration variable TIMES=2)
    -heroku config (see all config vars)
    -referencec: https://devcenter.heroku.com/articles/config-vars
16. Provision database
    -heroku config (shows db url config var)
    -heroku pg (shows db's info)
    -reference: https://devcenter.heroku.com/articles/getting-started-with-python#provision-a-database
    -reference: https://devcenter.heroku.com/articles/heroku-postgresql


# Flask API method 2
 -reference: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
    