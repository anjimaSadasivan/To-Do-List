from flask import Flask, render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) 
####### Database####### 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////c:users/anjima/Desktop/todo/todo.db'

db = SQLAlchemy(app) 

class Todo(db.Model): 
	id = db.Column(db.Integer, primary_key = True) 
	text = db.Column(db.String(200)) 
	complete = db.Column(db.Boolean) 

###### Route when nothing is specified in the url###### 
@app.route('/') 
def index(): 
	incomplete = Todo.query.filter_by(complete = False).all() 
	complete = Todo.query.filter_by(complete = True).all() 

	return render_template('index.html', 
	incomplete = incomplete, complete = complete) 

###### Adding items###### 
@app.route('/add', methods =['POST']) 
def add(): 
	todo = Todo(text = request.form['todoitem'], complete = False) 
	db.session.add(todo) 
	db.session.commit() 

###### Makes to stay on the same home page###### 
return redirect(url_for('index')) 

###### Complete items###### 
@app.route('/complete/<id>') 
def complete(id): 

	todo = Todo.query.filter_by(id = int(id)).first() 
	todo.complete = True
	db.session.commit() 
	###### Makes to stay on the same home page###### 

return redirect(url_for('index')) 

if __name__ == '__main__': 
	app.run(debug = True) 
