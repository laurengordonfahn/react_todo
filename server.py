from flask import (Flask, request, render_template, redirect, flash, session, jsonify)

from flask_debugtoolbar import DebugToolbarExtension

from sqlalchemy import (asc, desc) 

from model import *

from helper_functions import *

#for searlizing sqlalchemy objects
from flask_marshmallow import Marshmallow

from jinja2 import StrictUndefined

#for facebook sign in
import facebook
#for environmental variables for facebook API
import os


app = Flask(__name__)
#for marshmellow searliazer to work
ma = Marshmallow(app)

app.secret_key = "pouring monday"

@app.route('/')
def index():
    """Render index.html"""
    return render_template("index.html")


@app.route('/todo')
def intial_todo():
    """ Send Intial Todos from DB to render opening page """
    
    todos = gather_all_todos_from_db()
    
    todo_array = []
    for todo in todos:
        todo_array.append(format_todo(todo))

    print todo_array, "THIS IS THE TODO_ARRAY PRINTING"

    return jsonify(todo_array)


@app.route('/todo', methods=['POST'])
def new_todo():
    """ Add a new todo to the DB return all todo to javascript """

    content = request.form.get("content")

    print "THIS IS WHAT CONTENT IS WHEN IT ARRIVES FROM JS", content, type(content)

    todo = commit_todo_to_db(content)

    return jsonify(format_todo(todo))



@app.route('/todo/<id>', methods=['DELETE'])
def remove_todo():
    """ Remove a todo by id from the DB return nothing """

    pass

@app.route('/todo/check_mark/<id>', methods=['PUTS'])
def check_mark_todo():
    """ Checkmark a todo by id, update DB return nothing """

    pass







if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port=5000)