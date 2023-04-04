from server import app
from flask import render_template


@app.get('/')
def index():
    return render_template("index.html")


@app.errorhandler(404)
def error(e):
    return render_template("404.html"), 404


@app.get('/help')
def helpuser():
    return render_template('help.html')


@app.get('/login')
def login():
    return render_template("login.html")


@app.get('/job')
def job():
    return render_template("job.html")




