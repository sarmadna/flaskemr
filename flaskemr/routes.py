from flask import render_template, request, redirect
from flaskemr import app, db
from flaskemr.models import Client, Visit

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/all-clients", methods=["GET", "POST"])
def allclients():
    all_clients = Client.query.all()
    if request.method == "POST":
        fnm = request.form["fnm"]
        all_clients = Client.query.filter_by(fnm=fnm).all()
        return render_template("all-clients.html", title="All Clients", all_clients=all_clients)

    return render_template("all-clients.html", title="All Clients", all_clients=all_clients)

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

@app.route("/all-visits", methods=["GET", "POST"])
def all_visits():
    if request.method == "POST":
        pid = request.form["pid"]
        client = Client.query.filter_by(pid=pid).first()
        all_visits = Visit.query.filter_by(cid=pid).all()
        return render_template("all-visits.html", title="All Clients", client=client, all_visits=all_visits)

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
