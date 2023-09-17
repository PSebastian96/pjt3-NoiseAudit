import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# register function
@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("join"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("join.html")


# login function
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))
    return render_template("signin.html")


# profile template
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user_details = list(mongo.db.user_profile.find())

    if session["user"]:
        return render_template("profile.html", username=username, user_details=user_details)

    return redirect(url_for("signin"))


@app.route('/add_profile', methods=['GET', 'POST'])
def add_profile():
    if request.method == 'POST':
        profile_details = {
            "fname": request.form.get("fname"),
            "lname": request.form.get("lname"),
            "user_email": request.form.get("user_email"),
            "phone_num": request.form.get("phone_num"),
            "profile_by": session["user"]
        }
        mongo.db.user_profile.insert_one(profile_details)
        flash("Details Successfully Added")
        return redirect(url_for("profile"))
    return render_template("add_profile.html")


@app.route("/edit_profile/<profile_id>", methods=["GET", "POST"])
def edit_details(profile_id):
    if request.method == "POST":
        submit = {
            "fname": request.form.get("fname"),
            "lname": request.form.get("lname"),
            "user_email": request.form.get("user_email"),
            "phone_num": request.form.get("phone_num"),
            "profile_by": session["user"]
        }
        mongo.db.user_profile.update_one({"_id": ObjectId(profile_id)}, {"$set": submit})
        flash("Details Successfully Updated")

    profile_details = mongo.db.user_profile.find_one({"_id": ObjectId(profile_id)})
    return render_template("edit_profile.html", profile_details=profile_details, _id=_id)

# sign out function
@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("signin"))


@app.route("/delete_user/<username>")
def delete_user(username):
    mongo.db.users.delete_one(username)
    flash("Account Has Been Deleted")
    return redirect(url_for("signin"))


@app.route("/get_blogs")
def get_blogs():
    return render_template("get_blogs.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
