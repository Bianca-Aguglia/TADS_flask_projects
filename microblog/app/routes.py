from app import app
from flask import render_template
from app.forms import LoginForm

user = {'username': 'Bianca'}

posts = [
    {'author': {'username': 'John'},
     'body': 'It\'s snowing ... again.'},
    {'author': {'username': 'Jane'},
     'body': 'It\'s Richard Feynmam\'s birthday today.'}]

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', title='Nth Microblog', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)