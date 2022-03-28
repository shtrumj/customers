from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY']= 'M&D5rk)J^h%tPJ8T'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

@app.route('/')
@app.route('/login')
def index():
    return render_template('login.html', title='Login')
@app.route('/signin')
def signin():
    return render_template('signin.html', title='Signin')
@app.route('/about')
def about():
    return render_template('about.html',title="About")
@app.route('/customers')
def customers():
    return render_template('customers.html',title="Customers")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
