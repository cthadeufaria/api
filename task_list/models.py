from task_list import db

class Task(db.Model):
    # Create table column: 'db.Column'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    # Create method to print information from class Drink's attributes stored in database
    def __repr__(self) -> str:
        return f"{self.name} - {self.description}"