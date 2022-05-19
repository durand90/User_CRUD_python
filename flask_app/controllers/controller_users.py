from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_user import User

@app.route('/user/new')
def new_table_name():
    return render_template('users_new.html')

@app.route('/user/create', methods=['post'])
def create_user():
    id = User.create(request.form)
    print(id)
    return redirect('/')

@app.route('/user/<int:id>')
def show_table_name(id):
    pass

@app.route('/user/<int:id>/edit')
def edit_user(id):
    user = User.get_one({'id': id})
    
    return render_template('user_edit.html', user = user)

@app.route('/user/<int:id>/update', methods=['post'])
def update_user(id):
    User.update_one(request.form)
    return redirect('/')

@app.route('/user/<int:id>/delete')
def delete_table_name(id):
    User.delete_one({ 'id':id })
    return redirect('/')
