import datetime
from flask import jsonify, request
from app import app, db
from app.models import User

@app.route("/users", methods=["POST"])
def new_user():
    # Accepts the following parameters:
    # - safe: true/false
    safe = request.json['safe']

    # Creates user in database and returns user id
    # to the frontend as json
    u = User(safe=safe)
    db.session.add(u)
    db.session.commit()
    return jsonify(user_id=u.id)

@app.route("/users/<id>", methods=["POST"])
def update_user(id):
    # Receives user details:
    # - id
    # Query database User object using id:
    u = User.query.get(id)
    # - Updates full_name
    u.full_name = request.json['full_name']
    # - Updates date_of_birth
    u.date_of_birth = datetime.datetime.strptime(request.json['date_of_birth'], "%d/%m/%Y").date()
    db.session.add(u)
    db.session.commit()
    # Updates the user in the database and returns success
    return jsonify(success=True)

@app.route("/users")
def users():
    # Returns a list of all users with all their details
    users = User.query.all()
    return jsonify(users=[u.serialize for u in users])
