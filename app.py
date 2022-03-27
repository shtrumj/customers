from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY']= 'MySecretKey'

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/customers')
def customers():
    return render_template('customers.html')
if __name__ == '__main__':
    app.run(debug=True)
