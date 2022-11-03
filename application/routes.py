from application import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/experience')
def experience():
    return render_template("experience.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")