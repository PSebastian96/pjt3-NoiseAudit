import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_ckeditor import CKEditor
if os.path.exists("env.py"):
    import env

# flask instance
app = Flask(__name__)

# app config for db
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# mongo instance
mongo = PyMongo(app)

# ckeditor
ckeditor = CKEditor(app)


# home default page
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
            "password": generate_password_hash(request.form.get("password")),
            "fname": request.form.get("lname").lower(),
            "lname": request.form.get("fname").lower(),
            "user_email": request.form.get("user_email").lower()
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
    users = list(mongo.db.users.find())

    if session["user"]:
        return render_template(
            "profile.html", username=username, users=users)

    return redirect(url_for("signin"))


# edit profile details
@app.route("/edit_details/<user_id>", methods=["GET", "POST"])
def edit_details(user_id):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if request.method == "POST":
        submit = {
            "fname": request.form.get("fname"),
            "lname": request.form.get("lname"),
            "user_email": request.form.get("user_email")
        }
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": submit})
        flash("Task Successfully Updated")

    users = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("edit_profile.html", users=users, username=username)


# sign out function
@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("signin"))


# delete account
@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    # remove user from session cookie and from database
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("Account Has Been Deleted")
    session.pop("user")
    return redirect(url_for("index"))


# blog page template
@app.route("/get_blogs")
def get_blogs():
    return render_template("get_blogs.html")


# contact page template
@app.route("/contact")
def contact():
    return render_template("contact.html")


# admin dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
