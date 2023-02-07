from flask import render_template, request
from flaskemr import app
from flaskemr.models import Client, Visit

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/all-clients")
def allclients():
    allclients = Client.query.all()
    return render_template("all-clients.html", title="All Clients", allclients=allclients)

@app.route("/new-client")
def newclient():
    return render_template("new-client.html", title="New Client")

@app.route("/new-visit")
def newvisit():
    return render_template("new-visit.html", title="New Visit")

@app.route("/search")
def search():
    return render_template("/search.html", title="Search")

@app.route("/new-client-form")
def newclientform():
    return "new client form"

@app.route("/new-visit-form")
def newvisitform():
    return "new visit form"

@app.route("/search-form", methods=["GET", "POST"])
def searchform():
    if request.method == "POST":
        pid = request.form["pid"]
        fnm = request.form["fnm"]
        clientquery = Client.query.filter_by(pid=pid).first()
        visitquery = Visit.query.filter_by(cid=pid)
    return render_template("search-results.html", title="Search Results", clientquery=clientquery, visitquery=visitquery)