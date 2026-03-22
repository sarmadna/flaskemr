from flaskemr import db


# --- creates table for clients
class Client(db.Model):
    __tablename__ = "clients"

    pid = db.Column(db.Integer, primary_key=True)
    fnm = db.Column(db.String(20), nullable=False, index=True)
    mnm = db.Column(db.String(20), nullable=False)
    lnm = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    adr = db.Column(db.String(20), nullable=False)
    tel = db.Column(db.String(20), nullable=False)
    visits = db.relationship("Visit", backref="client", cascade="all, delete")

    def __init__(self, fnm, mnm, lnm, sex, dob, adr, tel):
        self.fnm = fnm
        self.mnm = mnm
        self.lnm = lnm
        self.sex = sex
        self.dob = dob
        self.adr = adr
        self.tel = tel

    @property
    def display_pid(self):
        return f"CL-{self.pid:04d}"

    def __repr__(self):
        return f"Client({self.fnm}, {self.mnm}, {self.lnm}, {self.sex}, {self.dob}, {self.adr}, {self.tel})"


# --- create table for visits
class Visit(db.Model):
    __tablename__ = "visits"

    vid = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, db.ForeignKey("clients.pid"), nullable=False)
    dat = db.Column(db.Date, nullable=False)
    ccc = db.Column(db.String(90), nullable=False)
    dxx = db.Column(db.String(90), nullable=False)
    rx1 = db.Column(db.String(90), nullable=False)
    rx2 = db.Column(db.String(90), nullable=False)
    rx3 = db.Column(db.String(90), nullable=False)
    rx4 = db.Column(db.String(90), nullable=False)

    def __init__(self, cid, dat, ccc, dxx, rx1, rx2, rx3, rx4):
        self.dat = dat
        self.ccc = ccc
        self.dxx = dxx
        self.rx1 = rx1
        self.rx2 = rx2
        self.rx3 = rx3
        self.rx4 = rx4
        self.cid = cid

    @property
    def display_vid(self):
        year = self.dat.year
        return f"VT-{year}-{self.vid:04d}"

    def __repr__(self):
        return f"Visit({self.cid}, {self.dat}, {self.ccc}, {self.dxx}, {self.rx1}, {self.rx2}, {self.rx3}, {self.rx4})"
    