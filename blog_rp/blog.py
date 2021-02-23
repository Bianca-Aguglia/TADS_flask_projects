from flask import Flask, render_template, request, session
from flask import flash, redirect, url_for, g

DATABASE = 'blog.db'

app = Flask(__name__)

app.config.from_obj(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)



