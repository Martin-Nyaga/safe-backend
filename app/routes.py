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
    id = request.args.get('id')
    # Query database User object using id:
    u = User.query.filter_by(id=id)
    # - Updates full_name
    u.full_name = request.json['full_name']
    # - Updates date_of_birth
    u.date_of_birth = request.json['date_of_birth']
    db.session.commit()
    # Updates the user in the database and returns success
    return jsonify(success=True)

@app.route("/users")
def users():

    return 'list users'
    # Returns a list of all users with all their details
    # Unknown for users whose names are unknown
