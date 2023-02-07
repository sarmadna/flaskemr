from flaskemr import db

class Client(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    fnm = db.Column(db.String(20), nullable=False)
    mnm = db.Column(db.String(20), nullable=False)
    lnm = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Integer, primary_key=True)
    mob = db.Column(db.String(20), nullable=False)
    visits = db.relationship("Visit")

    def __repr__(self):
        return f"Client({self.pid}, {self.fnm}, {self.mnm}, {self.lnm}, {self.sex}, {self.dob}, {self.mob})"

class Visit(db.Model):
    vid = db.Column(db.Integer, primary_key=True)
    dov = db.Column(db.Integer, nullable=False)
    mov = db.Column(db.Integer, nullable=False)
    yov = db.Column(db.Integer, nullable=False)
    cc = db.Column(db.String(50), nullable=False)
    dx = db.Column(db.String(50), nullable=False)
    rx1 = db.Column(db.String(50), nullable=False)
    rx2 = db.Column(db.String(50), nullable=False)
    rx3 = db.Column(db.String(50), nullable=False)
    rx4 = db.Column(db.String(50), nullable=False)
    cid = db.Column(db.Integer, db.ForeignKey("client.pid"), nullable=False)

    def __repr__(self):
        return f"Visit({self.vid}, {self.cid}, {self.dov}, {self.mov}, {self.yov}, {self.cc}, {self.dx}, {self.rx1}, {self.rx2}, {self.rx3}, {self.rx4})"
    