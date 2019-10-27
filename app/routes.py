import datetime, json
from flask import jsonify, request
from app import app, db
from app.models import User

@app.route("/users", methods=["POST"])
def new_user():
    # Accepts the following parameters:
    # Safe Boolean Value: true/false
    safe = request.json.get('safe')
    # Request latitude, longitude from frontend/user
    latitude = request.json.get('latitude')
    longitude = request.json.get('longitude')
    # Creates user in database and returns user id
    # to the frontend as json
    u = User(safe=safe, latitude=latitude, longitude=longitude)
    db.session.add(u)
    db.session.commit()
    return jsonify(user_id=u.id)

@app.route("/users/<id>", methods=["POST"])
def update_user(id):
    u = User.query.get(id)

    full_name = request.json.get('full_name')
    if full_name != None:
        u.full_name = full_name

    date_of_birth = request.json.get('date_of_birth')
    if date_of_birth != None:
        u.date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()

    safe = request.json.get('safe')
    if safe != None:
        u.safe = safe

    db.session.add(u)
    db.session.commit()
    return jsonify(success=True)

@app.route("/users")
def users():
    # Returns a list of all users with all their details
    users = User.query.all()
    return jsonify(users=[u.serialize for u in users])

@app.route("/guidance")
def guidance():
    # Reads json and sends to frontend using jsonify
    # file_name = os.path.join(app.static, 'disastersteps.json')
    with open('disastersteps.json') as guidance_json:
        data = json.load(guidance_json)
        return jsonify(data)
