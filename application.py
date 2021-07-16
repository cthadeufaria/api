# Setting up Flask
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


# Pass database configuration to flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Create class to manage database importing from db.Model
class Drink(db.Model):
    # Create table column: 'db.Column'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    # Create method to print information from class Drink's attributes stored in database
    def __repr__(self) -> str:
        return f"{self.name} - {self.description}"


# Create route (endpoint)
@app.route('/')
def index():
    return 'Welcome to the API main endpoint.'


# Create GET request
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []

    for drink in drinks:
        drink_data = {
            'name' : drink.name, 
            'description' : drink.description,
        }
        output.append(drink_data)

    return {'drinks' : output}


# Get specific table information by id
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)

    return {
        'name' : drink.name,
        'description' : drink.description,
    }


# Insert new information in table
@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.args.get('name'), description=request.args.get('description'))
    db.session.add(drink)
    db.session.commit()

    return {'id' : drink.id}


# Delete specific table information by id
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {'error' : 'drink not found'}
    db.session.delete(drink)
    db.session.commit()

    return {'message' : f"drink {drink.id} deleted"}
