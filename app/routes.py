import datetime, json
from flask import jsonify, request
from app import app, db
from app.utils import distance
from app.models import User, Post

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
    return jsonify(user=u.serialize)

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

    content = request.json.get('post_content')
    if content != None:
        add_post(content, u.id)

    db.session.add(u)
    db.session.commit()
    return jsonify(user=u.serialize)

@app.route("/users")
def users():
    # Returns a list of all users with all their details
    # users = User.query.all().order_by(distance({self.latitude, self.longitude},{latitude, longitude}))
    users = User.query.all()
    return jsonify(users=[u.serialize for u in users])

@app.route("/guidance")
def guidance():
    # Reads json and sends to frontend using jsonify
    with open('disastersteps.json') as guidance_json:
        data = json.load(guidance_json)
        return jsonify(data)


@app.route("/users/<user_id>/posts", methods=["POST"])
def create_post(user_id):
    content = request.json.get('content')
    add_post(content, user_id)
    user = User.query.get(user_id)
    return jsonify(user=user.serialize)

# Helper function
def add_post(content, user_id):
    p = Post(user_id=user_id, content=content,timestamp=datetime.datetime.now())
    db.session.add(p)
    db.session.commit()
