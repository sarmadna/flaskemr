from flask import render_template, request, redirect, url_for
from flaskemr import app, db
from flaskemr.models import Client, Visit


# --- this section shows the homepage
@app.route("/")
def home():
    return render_template("home.html", title="Home")


# --- this section shows all clients also filters clients by firstname
@app.route("/clients", methods=["GET", "POST"])
def allClients():
    if request.method == "POST":
        fnm = request.form.get("fnm", "").strip()
        all_clients = Client.query.filter(Client.fnm.ilike(f"{fnm}%")).all()
    else:
        all_clients = Client.query.all()

    return render_template("all-clients.html", title="Clients", all_clients=all_clients)


# --- this section shows new client form
@app.route("/clients/new")
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
    pid=new_client.pid
    return redirect(f"/clients/{pid}")


# --- this section shows client profile
@app.route("/clients/<int:pid>")
def clientProfile(pid):
    client = Client.query.get_or_404(pid)
    return render_template(
        "client-profile.html",
        title="Client Profile",
        client=client
    )


# --- this section deletes client data
@app.route("/clients/<int:pid>/remove", methods=["POST"])
def delClient(pid):
    deleted_client = Client.query.get_or_404(pid)
    db.session.delete(deleted_client)
    db.session.commit()
    return redirect(url_for("allClients"))


# --- this section shows all visits of a client
@app.route("/clients/<int:pid>/visits")
def allVisits(pid):
    client = Client.query.get_or_404(pid)
    all_visits = Visit.query.filter_by(cid=pid).order_by(Visit.vid.desc()).all()
    return render_template("all-visits.html", title="Visits", client=client, all_visits=all_visits)


# --- this section shows new visit form
@app.route("/clients/<int:pid>/visits/new")
def newVisit(pid):
    client = Client.query.get_or_404(pid)
    return render_template(
        "new-visit.html",
        title="New Visit",
        client=client
    )


# --- this section handles new visit data
@app.route("/new-visit-form", methods=["POST"])
def newVisitForm():
    data = request.form
    pid = int(data.get("pid"))
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
    return redirect(url_for("allVisits", pid=pid))


# --- this section deletes a visit
@app.route("/clients/<int:pid>/visits/remove/<int:vid>", methods=["POST"])
def delVisit(pid, vid):
    deleted_visit = Visit.query.get_or_404(vid)
    db.session.delete(deleted_visit)
    db.session.commit()
    return redirect(f"/clients/{pid}/visits")