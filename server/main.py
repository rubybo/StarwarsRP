

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


@app.get('/history')
def history():
    return render_template("hist.html")


@app.get('/docs')
def docs():
    return render_template("docs.html")


@app.get('/news')
def news():
    return render_template("news.html")









