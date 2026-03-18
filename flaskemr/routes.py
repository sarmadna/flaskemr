from flask import render_template, request, redirect, url_for
from flaskemr import app, db
from flaskemr.models import Client, Visit


# --- this section shows the home page
@app.route("/")
def home():
    total_clients = Client.query.count()
    total_visits = Visit.query.count()
    
    recent_clients = Client.query.order_by(Client.pid.desc()).limit(4)
    recent_visits = Visit.query.order_by(Visit.vid.desc()).limit(4)

    return render_template(
        "home.html", 
        title="Dashboard",
        total_clients=total_clients,
        total_visits=total_visits,
        recent_clients=recent_clients,
        recent_visits=recent_visits
        )


# --- this section shows all clients also filters clients by first name
@app.route("/clients/list", methods=["GET", "POST"])
def clients_list():
    if request.method == "POST":
        fnm = request.form.get("fnm", "").strip()
        all_clients = Client.query.filter(Client.fnm.ilike(f"{fnm}%")).all()
    else:
        all_clients = Client.query.all()

    return render_template("clients-list.html", title="Clients", all_clients=all_clients)


# --- this section shows new client form
@app.route("/clients/add")
def clients_add():
    return render_template("clients-add.html", title="Add Clients")


# --- this section handles new client form data
@app.route("/clients/add/form", methods=["POST"])
def clients_add_form():
    data = request.form
    new_client = Client(
        fnm=data.get("fnm"),
        mnm=data.get("mnm"),
        lnm=data.get("lnm"),
        sex=data.get("sex"),
        dob=data.get("dob"),
        adr=data.get("adr"),
        tel=data.get("tel")
    )
    db.session.add(new_client)
    db.session.commit()
    pid=new_client.pid
    return redirect(f"/clients/{pid}/profile")


# --- this section shows client profile
@app.route("/clients/<int:pid>/profile")
def clients_profile(pid):
    client = Client.query.get_or_404(pid)
    return render_template(
        "clients-profile.html",
        title="Profile",
        client=client
    )


# --- this section deletes client data
@app.route("/clients/<int:pid>/remove", methods=["POST"])
def clients_remove(pid):
    deleted_client = Client.query.get_or_404(pid)
    db.session.delete(deleted_client)
    db.session.commit()
    return redirect(url_for("clients_list"))


# --- this section shows all visits of a client
@app.route("/clients/<int:pid>/visits/list")
def visits_list(pid):
    client = Client.query.get_or_404(pid)
    all_visits = Visit.query.filter_by(cid=pid).order_by(Visit.vid.desc()).all()
    return render_template("visits-list.html", title="Visits", client=client, all_visits=all_visits)


# --- this section shows new visit form
@app.route("/clients/<int:pid>/visits/add")
def visits_add(pid):
    client = Client.query.get_or_404(pid)
    return render_template(
        "visits-add.html",
        title="Add Visits",
        client=client
    )


# --- this section handles new visit data
@app.route("/visits/add/form", methods=["POST"])
def visits_add_form():
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
    return redirect(url_for("visits_list", pid=pid))


# --- this section deletes a visit
@app.route("/clients/<int:pid>/visits/remove/<int:vid>", methods=["POST"])
def visits_remove(pid, vid):
    deleted_visit = Visit.query.get_or_404(vid)
    db.session.delete(deleted_visit)
    db.session.commit()
    return redirect(f"/clients/{pid}/visits/list")