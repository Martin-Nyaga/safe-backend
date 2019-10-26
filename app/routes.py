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
def update_user():
    return 'update user'
    # Receives user details:
    # - id
    # - full_name
    # - date_of_birth
    # Updates the user in the database and returns success

@app.route("/users")
def users():
    return 'list users'
    # Returns a list of all users with all their details
    # Unknown for users whose names are unknown
