from flask import render_template, request, redirect
from flaskemr import app, db
from flaskemr.models import Client, Visit
import psycopg2

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

@app.route("/new-client-form", methods=["GET", "POST"])
def newclientform():
    if request.method == "POST":
        fnm = request.form["fnm"]
        mnm = request.form["mnm"]
        lnm = request.form["lnm"]
        sex = request.form["sex"]
        dob = request.form["dob"]
        adr = request.form["adr"]
        mob = request.form["mob"]
        new_client = Client(fnm, mnm, lnm, sex, dob, adr, mob)
        db.session.add(new_client)
        db.session.commit()
        cid = new_client.pid
        dov = request.form["dov"]
        mov = request.form["mov"]
        yov = request.form["yov"]
        cc = request.form["cc"]
        dx = request.form["dx"]
        rx1 = request.form["rx1"]
        rx2 = request.form["rx2"]
        rx3 = request.form["rx3"]
        rx4 = request.form["rx4"]
        new_client_first_visit = Visit(cid, dov, mov, yov, cc, dx, rx1, rx2, rx3, rx4)
        db.session.add(new_client_first_visit)
        db.session.commit()
        return redirect("/new-client")

@app.route("/new-visit")
def newvisit():
    return render_template("new-visit.html", title="New Visit")

@app.route("/new-visit-form", methods=["GET", "POST"])
def newvisitform():
    if request.method == "POST":
        cid = request.form["pid"]
        dov = request.form["dov"]
        mov = request.form["mov"]
        yov = request.form["yov"]
        cc = request.form["cc"]
        dx = request.form["dx"]
        rx1 = request.form["rx1"]
        rx2 = request.form["rx2"]
        rx3 = request.form["rx3"]
        rx4 = request.form["rx4"]
        new_visit = Visit(cid, dov, mov, yov, cc, dx, rx1, rx2, rx3, rx4)
        db.session.add(new_visit)
        db.session.commit()
        return redirect("/new-visit")

@app.route("/search")
def search():
    return render_template("/search.html", title="Search")

@app.route("/search-form", methods=["GET", "POST"])
def searchform():
    if request.method == "POST":
        pid = request.form["pid"]
        fnm = request.form["fnm"]
        conn = psycopg2.connect(
            host = "localhost",
            database = "clinic",
            user = "postgres",
            password = "postgres"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM client_visit_view WHERE pid = %s", (pid))
        search_query = cur.fetchall()
        return render_template("search-results.html", title="Search Result", search_query=search_query)
