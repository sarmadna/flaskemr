from flask import render_template, request, redirect, url_for
from flaskemr import app, db
from flaskemr.models import Client, Visit
from datetime import datetime


# --- this section shows the home page
@app.route("/")
def home():
    total_clients = Client.query.count()
    total_visits = Visit.query.count()
    
    recent_clients = Client.query.order_by(Client.pid.desc()).limit(4).all()
    recent_visits = Visit.query.order_by(Visit.dat.desc()).limit(4).all()

    return render_template(
        "home.html", 
        title="Dashboard",
        total_clients=total_clients,
        total_visits=total_visits,
        recent_clients=recent_clients,
        recent_visits=recent_visits
        )


# ########## CLIENTS SECTION ##########

# --- this section shows all clients also searches clients by first name
@app.route("/clients/list", methods=["GET", "POST"])
def clients_list():
    if request.method == "POST":
        fnm = request.form.get("fnm", "").strip()
        all_clients = Client.query.filter(Client.fnm.ilike(f"{fnm}%")).all()
    else:
        all_clients = Client.query.all()

    return render_template("clients-list.html", title="Clients", all_clients=all_clients)


# --- this section handles new client form and data
@app.route("/clients/add", methods=["GET", "POST"])
def clients_add():
    if request.method == "POST":
        data = request.form
        date_str = data.get("dob")
        dob = datetime.strptime(date_str, "%Y-%m-%d").date()
        new_client = Client(
            fnm=data.get("fnm"),
            mnm=data.get("mnm"),
            lnm=data.get("lnm"),
            sex=data.get("sex"),
            dob=dob,
            adr=data.get("adr"),
            tel=data.get("tel")
        )
        db.session.add(new_client)
        db.session.commit()
        pid=new_client.pid
        return redirect(url_for('clients_profile', pid=pid))
    else:
        return render_template("clients-add.html", title="Add Clients")



# --- this section shows client profile
@app.route("/clients/<int:pid>/profile")
def clients_profile(pid):
    client = Client.query.get_or_404(pid)
    return render_template(
        "clients-profile.html",
        title="Profile",
        client=client
    )


# --- this section handle client edit form and data
@app.route("/clients/<int:pid>/edit", methods=["GET", "POST"])
def clients_edit(pid):
    client = Client.query.get_or_404(pid)
    if request.method == "POST":
        data = request.form
        client.fnm = data.get("fnm")
        client.mnm = data.get("mnm")
        client.lnm = data.get("lnm")
        client.sex = data.get("sex")
        date_str = data.get("dob")
        client.dob = datetime.strptime(date_str, "%Y-%m-%d").date()
        client.adr = data.get("adr")
        client.tel = data.get("tel")
        db.session.commit()
        return redirect(url_for("clients_profile", pid=pid))
    else:
        return render_template("clients-edit.html", title="Edit client", client=client)


# --- this section deletes client data
@app.route("/clients/<int:pid>/remove", methods=["POST"])
def clients_remove(pid):
    deleted_client = Client.query.get_or_404(pid)
    db.session.delete(deleted_client)
    db.session.commit()
    return redirect(url_for("clients_list"))


# ########## VISITS SECTION ##########

# --- this section shows all visits of a client
@app.route("/clients/<int:pid>/visits/list")
def visits_list(pid):
    client = Client.query.get_or_404(pid)
    all_visits = Visit.query.filter_by(cid=pid).order_by(Visit.vid.desc()).all()
    return render_template("visits-list.html", title="Visits", client=client, all_visits=all_visits)


# --- this section handles new visit data
@app.route("/clients/<int:pid>/visits/add", methods=["GET", "POST"])
def visits_add(pid):
    if request.method == "POST":
        data = request.form
        pid = int(data.get("pid"))

        date_str = data.get("dat")
        dat = datetime.strptime(date_str, "%Y-%m-%d").date()

        new_visit = Visit(
            cid=data.get("pid"),
            dat=dat,
            ccc=data.get("ccc"),
            dxx=data.get("dxx"),
            rx1=data.get("rx1"),
            rx2=data.get("rx2"),
            rx3=data.get("rx3"),
            rx4=data.get("rx4")
        )
        db.session.add(new_visit)
        db.session.commit()
        return redirect(url_for("visits_list", pid=pid))
    else:
        client = Client.query.get_or_404(pid)
        return render_template(
            "visits-add.html",
            title="Add Visits",
            client=client
        )


# --- this section views visits card
@app.route("/clients/<int:pid>/visits/<int:vid>/card")
def visits_card(pid, vid):
    visit = Visit.query.get_or_404(vid)
    return render_template("visits-card.html", title="Visit card", visit=visit)


# --- this section handles visit edits
@app.route("/clients/<int:pid>/visits/<int:vid>/edit", methods=["GET", "POST"])
def visits_edit(pid, vid):
    visit = Visit.query.get_or_404(vid)
    if request.method == "POST":
        data = request.form
        date_str = data.get("dat")
        visit.cid = visit.client.pid
        visit.dat = datetime.strptime(date_str, "%Y-%m-%d").date()
        visit.ccc = data.get("ccc")
        visit.dxx = data.get("dxx")
        visit.rx1 = data.get("rx1")
        visit.rx2 = data.get("rx2")
        visit.rx3 = data.get("rx3")
        visit.rx4 = data.get("rx4")
        db.session.commit()
        return redirect(url_for("visits_card", pid=pid, vid=vid))
    else:
        return render_template("visits-edit.html", title="Card edit", visit=visit)


# --- this section removes a visit
@app.route("/clients/<int:pid>/visits/<int:vid>/remove", methods=["POST"])
def visits_remove(pid, vid):
    deleted_visit = Visit.query.get_or_404(vid)
    db.session.delete(deleted_visit)
    db.session.commit()
    return redirect(f"/clients/{pid}/visits/list")
