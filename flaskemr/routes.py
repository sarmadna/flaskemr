from flask import render_template, request, redirect
from flaskemr import app, db
from flaskemr.models import Client, Visit


# --- this section renders the homepage
@app.route("/")
def home():
    return render_template("home.html", title="Home")


# --- this section shows all clients also filters clients by firstname
@app.route("/all-clients", methods=["GET", "POST"])
def allClients():
    if request.method == "POST":
        fnm = request.form.get("fnm", "").strip()
        all_clients = Client.query.filter(Client.fnm.ilike(f"{fnm}%")).all()
    else:
        all_clients = Client.query.all()

    return render_template("all-clients.html", title="Clients", all_clients=all_clients)


# --- this section renders new client form
@app.route("/new-client")
def newClient():
    return render_template("new-client.html", title="New Client")


# --- this section handles new client form data
@app.route("/new-client-form", methods=["POST"])
def newClientForm():
    data = request.form
    new_client = Client(
        fnm=data.get("fnm"),
        mnm=data.get("mnm"),
        lnm=data.get("lnm"),
        sex=data.get("sex"),
        dob=data.get("dob"),
        adr=data.get("adr"),
        mob=data.get("mob")
    )
    db.session.add(new_client)
    db.session.commit()
    return redirect("/new-client")


# --- this section deletes client data
@app.route("/del-client", methods=["POST"])
def delClient():
    pid = request.form.get("pid")
    Visit.query.filter_by(cid=pid).delete()
    Client.query.filter_by(pid=pid).delete()
    db.session.commit()
    return redirect("/all-clients")


# --- this section shows all visits of a client
@app.route("/all-visits", methods=["POST"])
def allVisits():
    pid = request.form.get("pid")
    client = Client.query.filter_by(pid=pid).first()
    all_visits = Visit.query.filter_by(cid=pid).all()
    return render_template("all-visits.html", title="Visits", client=client, all_visits=all_visits)


# --- this section renders new visit form
@app.route("/new-visit")
def newVisit():
    return render_template("new-visit.html", title="New Visit")


# --- this section handles new visit data
@app.route("/new-visit-form", methods=["POST"])
def newVisitForm():
    data = request.form
    new_visit = Visit(
        cid=data.get("pid"),
        dov=data.get("dov"),
        mov=data.get("mov"),
        yov=data.get("yov"),
        cc=data.get("cc"),
        dx=data.get("dx"),
        rx1=data.get("rx1"),
        rx2=data.get("rx2"),
        rx3=data.get("rx3"),
        rx4=data.get("rx4")
    )
    db.session.add(new_visit)
    db.session.commit()
    return redirect("/new-visit")


# --- this section deletes a visit
@app.route("/del-visit", methods=["POST"])
def delVisit():
    vid = request.form.get("vid")
    Visit.query.filter_by(vid=vid).delete()
    db.session.commit()
    return redirect("/all-clients")