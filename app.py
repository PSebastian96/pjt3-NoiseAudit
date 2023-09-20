import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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
    list_of_blogs = list(mongo.db.blogsdb.find())
    return render_template("get_blogs.html", list_of_blogs=list_of_blogs)


# read blog
@app.route("/blog/<blog_id>")
def read_blog(blog_id):
    blog = mongo.db.blogsdb.find_one({"_id": ObjectId(blog_id)})
    return render_template("get_blogs.html", blog=blog)


# add blog function
@app.route("/add_blog", methods=["GET", "POST"])
def add_blog():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    now = datetime.now() # current date and time
    date_time = now.strftime("%d/%m/%Y")
    
    if request.method == "POST":
        blog = {
            "created_by": session["user"],
            "created_date": request.form.get("created_date"),
            "blog_title": request.form.get("blog_title"),
            "blog_content": request.form.get("blog_content")
        }
        mongo.db.blogsdb.insert_one(blog)
        flash("Audit Successfully Published")
        return redirect(url_for("get_blogs"))

    list_of_blogs = mongo.db.categories.find().sort("created_date", 1)
    return render_template("add_blog.html", list_of_blogs=list_of_blogs, username=username, date_time=date_time)


# edit blog function
@app.route("/edit_blog/<blog_id>")
def edit_blog(blog_id):
    if request.method == "POST":
        submit = {
            "blog_title": request.form.get("blog_title"),
            "blog_content": request.form.get("blog_content")
        }
        mongo.db.blogsdb.update_one({"_id": ObjectId(blog_id)}, {"$set": submit})
        flash("Blog Successfully Edited")

    blog = mongo.db.blogsdb.find_one({"_id": ObjectId(blog_id)})
    return render_template("edit_blog.html", blog=blog)


# delete blog function
@app.route("/delete_blog/<blog_id>")
def delete_blog(blog_id):
    mongo.db.blogsdb.delete_one({"_id": ObjectId(blog_id)})
    flash("Audit Successfully Deleted")
    return redirect(url_for("get_blogs"))


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
