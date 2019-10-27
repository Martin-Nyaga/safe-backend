from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120))
    date_of_birth = db.Column(db.Date)
    safe = db.Column(db.Boolean)

    def __repr__(self):
        return '<User {}: {}>'.format(self.full_name, self.date_of_birth)

    def full_name_or_unknown(self):
        if self.full_name:
            return self.full_name
        else:
            return "Unknown User"

    def date_of_birth_or_unknown(self):
        if self.date_of_birth:
            return self.date_of_birth.strftime("%d/%m/%Y")
        else:
            return "Unknown Date of Birth"

    @property
    def serialize(self):
       return {
           'id': self.id,
           'full_name': self.full_name_or_unknown(),
           'safe': self.safe,
           'date_of_birth': self.date_of_birth_or_unknown()
       }

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
