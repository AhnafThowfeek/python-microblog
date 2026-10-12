from flask import render_template
from app import app
from app.form import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ahnaf'}
    posts = [
        {
            'author': {'username': 'Jhon'},
            'body': 'Good day'
        },
        {
            'author': {'username': 'asd'},
            'body': 'nice day'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
