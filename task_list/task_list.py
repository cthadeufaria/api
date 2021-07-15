from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from task_list import db
from task_list.models import Drink

bp = Blueprint('task_list', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        if not name:
            flash('Drink name is required.')
        else:
            db.session.add(Drink(name=name, description=description))
            db.session.commit()

    tasks = Drink.query.all()
    return render_template('task_list/index.html', tasks=tasks)

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    task = Drink.query.get(id)
    if task != None:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('task_list.index'))
