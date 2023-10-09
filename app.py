import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_ckeditor import CKEditor
if os.path.exists("env.py"):
    import env

# flask instance
app = Flask(__name__)

# ckeditor instance
ckeditor = CKEditor(app)

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
            "user_email": request.form.get("user_email").lower(),
            "bookmarks": []
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
    # display blogs by latest date
    list_of_blogs = list(mongo.db.blogsdb.find().sort("created_date", -1))
    return render_template("get_blogs.html", list_of_blogs=list_of_blogs)


# search blogs
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        list_of_blogs = list(mongo.db.blogsdb.find({"$text":
                                                   {"$search": query}}))
        return render_template("get_blogs.html", list_of_blogs=list_of_blogs)


# read blog
@app.route("/read_blog/<blog_id>")
def read_blog(blog_id):
    current_user = session.get('user')
    list_of_users = list(mongo.db.users.find())
    list_of_blogs = mongo.db.blogsdb.find_one({"_id": ObjectId(blog_id)})
    # get admin value from db
    admin_user = mongo.db.users.find_one({"username": "admin"})
    list_of_comments = list(mongo.db.commentsdb.find().sort('comm_date', 1))
    # match the comment to the correct blog
    related_comment = list(mongo.db.commentsdb.find({'comm_id': blog_id}).sort(
                                                    'comm_date', 1))
    # check if user doesn't exist in database 
    if current_user is None:
        flash("Please login to complete request!")
        return redirect(url_for("index"))
    # if logged in
    else:
        return render_template("read_blog.html", list_of_blogs=list_of_blogs,
                               list_of_comments=list_of_comments,
                               related_comment=related_comment,
                               admin_user=admin_user,
                               current_user=current_user)


# add blog function
@app.route("/add_blog", methods=["GET", "POST"])
def add_blog():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    now = datetime.now()  # current date and time
    date_time = now.strftime("%d/%m/%Y")

    current_user = session.get('user')

    if current_user is None:
        flash("Please login to complete request!")
        return redirect(url_for("index"))

    if request.method == "POST":
        # find blog's title
        blog_title = {
            "blog_title": request.form.get("blog_title").title()
        }

        blog = {
            "created_by": session["user"],
            "category_name": request.form.get("category_name"),
            "created_date": request.form.get("created_date"),
            "blog_title": request.form.get("blog_title"),
            "blog_content": request.form.get("ckeditor")
        }

        # check if blog exists by checking title
        existing_blog = mongo.db.blogsdb.find_one(blog_title)

        # if blog title exists tell user the it's already in the db
        if existing_blog:
            flash("Audit Title Already Exists.")

        # If it doesn't exist, post audit
        else:
            mongo.db.blogsdb.insert_one(blog)
            flash("Audit Successfully Published")
            return redirect(url_for("get_blogs"))

    list_of_blogs = mongo.db.blogsdb.find().sort("created_date", 1)
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_blog.html", list_of_blogs=list_of_blogs,
                           username=username, date_time=date_time,
                           categories=categories)


# edit blog function
@app.route("/edit_blog/<blog_id>", methods=["GET", "POST"])
def edit_blog(blog_id):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    now = datetime.now()  # current date and time
    date_time = now.strftime("%d/%m/%Y")

    current_user = session.get('user')

    if current_user is None:
        flash("Please login to complete request!")
        return redirect(url_for("index"))

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "blog_title": request.form.get("blog_title"),
            "created_date": request.form.get("created_date"),
            "blog_content": request.form.get("ckeditor")
        }
        mongo.db.blogsdb.update_one({"_id": ObjectId(blog_id)},
                                    {"$set": submit})
        flash("Blog Successfully Edited")

    blog = mongo.db.blogsdb.find_one({"_id": ObjectId(blog_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_blog.html", blog=blog, categories=categories,
                           date_time=date_time, username=username)


# delete blog function
@app.route("/delete_blog/<blog_id>")
def delete_blog(blog_id):
    current_user = session.get('user')

    if current_user is None:
        flash("Please login to complete request!")
        return redirect(url_for("index"))

    mongo.db.blogsdb.delete_one({"_id": ObjectId(blog_id)})
    flash("Audit Successfully Deleted")
    return redirect(url_for("get_blogs"))


# add comment
@app.route('/add_comment/<blog_id>', methods=['GET', 'POST'])
def add_comment(blog_id):
    now = datetime.now()  # current date and time
    date_time = now.strftime("%d/%m/%Y")

    current_user = session.get('user')

    if current_user is None:
        flash("Please login to complete request!")
        return redirect(url_for("index"))

    if request.method == 'POST':
        comment = {
            "comm_id": blog_id,
            "comm_date": date_time,
            "comm_content": request.form.get("comm_content").lower(),
            "comm_by": session["user"]
        }
        mongo.db.commentsdb.insert_one(comment)
        flash("Comment Successfully Added")
        return redirect(url_for('get_blogs'))

    list_of_blogs = mongo.db.blogsdb.find_one({"_id": ObjectId(blog_id)})
    return render_template('add_comment.html', list_of_blogs=list_of_blogs)


# edit comment
@app.route('/edit_comment/<comment_id>', methods=["GET", "POST"])
def edit_comment(comment_id):

    current_user = session.get('user')

    if current_user is None:
        flash("Please login to complete request!")
        return redirect(url_for("index"))

    if request.method == "POST":
        submit = {
            "comm_content": request.form.get("comm_content")
        }
        mongo.db.commentsdb.update_one({"_id": ObjectId(comment_id)},
                                       {"$set": submit})
        flash("Comment Successfully Updated")

    list_of_comments = mongo.db.commentsdb.find_one({"_id":
                                                    ObjectId(comment_id)})
    return render_template("edit_comment.html",
                           list_of_comments=list_of_comments)


# delete comment
@app.route('/delete_comment/<comment_id>')
def delete_comment(comment_id):

    current_user = session.get('user')

    if current_user is None:
        flash("Please login to complete request!")
        return redirect(url_for("index"))

    mongo.db.commentsdb.delete_one({"_id": ObjectId(comment_id)})
    flash("Comment Successfully Deleted")
    return redirect(url_for('get_blogs'))


# my blogs page
@app.route('/myblogs')
def my_blogs():

    current_user = session.get('user')

    if current_user is None:
        flash("Please login to complete request!")
        return redirect(url_for("index"))

    # display blogs by latest date
    list_of_blogs = list(mongo.db.blogsdb.find().sort("created_date", -1))
    return render_template("my_blogs.html", list_of_blogs=list_of_blogs)


# contact page template
@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")


# admin dashboard
@app.route("/dashboard")
def dashboard():
    list_of_users = list(mongo.db.users.find())
    list_of_blogs = list(mongo.db.blogsdb.find())
    admin_user = mongo.db.users.find_one({"username": "admin"})

    # current user's session
    current_user = session.get('user')

    if current_user is None:
        flash("Please login to complete request!")
        return redirect(url_for("index"))

    # find admin session
    admin_user = mongo.db.users.find_one({"username": "admin"})

    if current_user == admin_user:
        flash("You do not have permission to access this page!")
        return redirect(url_for("index"))

    else:
        return render_template("dashboard.html", list_of_users=list_of_users,
                           list_of_blogs=list_of_blogs)

    


# admin search function
@app.route("/admin_search", methods=["GET", "POST"])
def admin_search():
    if request.method == "POST":
        query = request.form.get("query")
        list_of_blogs = list(mongo.db.blogsdb.find({"$text":
                                                   {"$search": query}}))
        list_of_users = list(mongo.db.users.find({"$text":
                                                 {"$search": query}}))
        return render_template("dashboard.html", list_of_blogs=list_of_blogs,
                               list_of_users=list_of_users)


# admin remove account
@app.route("/delete_user_admin/<user_id>")
def delete_user_admin(user_id):
    admin_user = mongo.db.users.find_one({"username": "admin"})

    if admin_user:
        mongo.db.users.delete_one({"_id": ObjectId(user_id)})
        flash("Account Has Been Deleted")
        return redirect(url_for("dashboard"))
    else:
        flash("You do not have permission to access this page!")
        return redirect(url_for("index"))


# error handling 404 page not found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


# error handling 500 internal server error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
