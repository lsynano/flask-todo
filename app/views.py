from app import app, db
from flask import render_template, request
from app.models import Todo

@app.route('/', methods=['POST', 'GET'])
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route('/add', methods=['POST', 'GET'])
def add():
    print("adding...")
    form = request.form
    print(form)
    content = form['content']
    print(content)
    todo = Todo(content)
    db.session.add(todo)
    db.session.commit()
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route('/done/<todo_time>', methods=['POST', 'GET'])
def done(todo_time):
    todo = Todo.query.filter_by(time=todo_time).first()
    if todo is not None:
        todo.status = 1
        db.session.add(todo)
        db.session.commit()
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route('/undone/<todo_time>', methods=['POST', 'GET'])
def undone(todo_time):
    todo = Todo.query.filter_by(time=todo_time).first()
    if todo is not None:
        todo.status = 0
        db.session.add(todo)
        db.session.commit()
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route('/delete/<todo_time>', methods=['POST', 'GET'])
def delete(todo_time):
    todo = Todo.query.filter_by(time=todo_time).first()
    if todo is not None:
        db.session.delete(todo)
        db.session.commit()
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)
