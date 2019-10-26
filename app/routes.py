from app import app

@app.route("/users", methods=["POST"])
def new_user():
    # Accepts the following parameters:
    # - safe: true/false
    # Creates user in database and returns ID
    return 'new_user'

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
