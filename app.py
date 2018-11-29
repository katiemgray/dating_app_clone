from flask import Flask, render_template, request
from profile import myProfile

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route('/form')
def generate_form():
    return render_template("form.html")

@app.route('/profile_page')
def generate_profile():
    """ takes in input from from and renders profile template"""
    name = request.args['name']
    age = request.args['age']
    location = request.args['location']
    bio = request.args['bio']
    return render_template("profile_page.html", name=name, age=age, location=location, bio=bio)
