from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    # greetings = 'HI!'
    msg = 'Welcome to the API documentation page'
    endpoints = [{
        'name' : 'GET info',
        'description' : '/info/<id> Parameters: id (optional): info id to be retrieved', 
    }, {
        'name' : 'POST info',
        'description' : '/info Parameters: None',
    }, {
        'name' : 'DELETE info',
        'description' : '/info/<id> Parameters: id: info id to be deleted',
    }]
    return render_template('index.html' , greetings=None, msg=msg, endpoints=endpoints)


# # Create GET request
# @app.route('/drinks')
# def get_drinks():
#     drinks = Drink.query.all()
#     output = []

#     for drink in drinks:
#         drink_data = {
#             'name' : drink.name, 
#             'description' : drink.description,
#         }
#         output.append(drink_data)

#     return {'drinks' : output}


# # Get specific table information by id
# @app.route('/drinks/<id>')
# def get_drink(id):
#     drink = Drink.query.get_or_404(id)

#     return {
#         'name' : drink.name,
#         'description' : drink.description,
#     }


# # Insert new information in table
# @app.route('/drinks', methods=['POST'])
# def add_drink():
#     drink = Drink(name=request.args.get('name'), description=request.args.get('description'))
#     db.session.add(drink)
#     db.session.commit()

#     return {'id' : drink.id}


# # Delete specific table information by id
# @app.route('/drinks/<id>', methods=['DELETE'])
# def delete_drink(id):
#     drink = Drink.query.get(id)
#     if drink is None:
#         return {'error' : 'drink not found'}
#     db.session.delete(drink)
#     db.session.commit()

#     return {'message' : f"drink {drink.id} deleted"}
