from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120))
    date_of_birth = db.Column(db.Date)
    safe = db.Column(db.Boolean)

    def __repr__(self):
        return '<User {}: {}>'.format(self.full_name, self.date_of_birth)
