from flaskemr import db

class Client(db.Model):
    __tablename__ = "client"

    pid = db.Column(db.Integer, primary_key=True)
    fnm = db.Column(db.String(20), nullable=False)
    mnm = db.Column(db.String(20), nullable=False)
    lnm = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Integer, nullable=False)
    adr = db.Column(db.String(20), nullable=False)
    mob = db.Column(db.String(20), nullable=False)
    visits = db.relationship("Visit")

    def __init__(self, fnm, mnm, lnm, sex, dob, adr, mob):
        self.fnm = fnm
        self.mnm = mnm
        self.lnm = lnm
        self.sex = sex
        self.dob = dob
        self.adr = adr
        self.mob = mob

    def __repr__(self):
        return f"Client({self.fnm}, {self.mnm}, {self.lnm}, {self.sex}, {self.dob}, {self.adr}, {self.mob})"

class Visit(db.Model):
    __tablename__ = "visit"

    vid = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, db.ForeignKey("client.pid"), nullable=False)
    dov = db.Column(db.Integer, nullable=False)
    mov = db.Column(db.Integer, nullable=False)
    yov = db.Column(db.Integer, nullable=False)
    cc = db.Column(db.String(50), nullable=False)
    dx = db.Column(db.String(50), nullable=False)
    rx1 = db.Column(db.String(50), nullable=False)
    rx2 = db.Column(db.String(50), nullable=False)
    rx3 = db.Column(db.String(50), nullable=False)
    rx4 = db.Column(db.String(50), nullable=False)

    def __init__(self, cid, dov, mov, yov, cc, dx, rx1, rx2, rx3, rx4):
        self.dov = dov
        self.mov = mov
        self.yov = yov
        self.cc = cc
        self.dx = dx
        self.rx1 = rx1
        self.rx2 = rx2
        self.rx3 = rx3
        self.rx4 = rx4
        self.cid = cid

    def __repr__(self):
        return f"Visit({self.cid}, {self.dov}, {self.mov}, {self.yov}, {self.cc}, {self.dx}, {self.rx1}, {self.rx2}, {self.rx3}, {self.rx4})"
    