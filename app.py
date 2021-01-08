import os
import datetime
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
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

"""
Pulls slang from the words collection in database
"""

@app.route("/")
@app.route("/get_words")
def get_words():
    # Sorts slang alphabetically
    words = list(mongo.db.words.find().sort("slang_term"))
    return render_template("words.html", words=words)


"""
Creates user and adds to database under user collection
"""


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks db to see if user already in use
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash(
                "Oops! Must be a Cadbury Flake. That Username already exists")
            return redirect(url_for("register"))
        # Generates a hashed password for security and stores in database
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Places new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Lovely jubley. Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


"""
Allows users to log in to site, captures incorrect
username/password, if credentials match, logs user in.
"""


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Checks db to see if user already in use
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Checks if hashed password matches user password
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("{}, alright guv'nor?".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # Password incorrect
                flash("It's all gone Pete Tong, Username/Password is wrong")
                return redirect(url_for("login"))

        else:
            # If the Username doesn't exist
            flash("It's all gone Pete Tong, Username/Password is wrong")
            return redirect(url_for("login"))

    return render_template("login.html")


"""
User profile page, checks what user is logged in via session user.
"""


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # If user log on credentials correct allows access to their profile page
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


"""
Logs user out of their account, returns to login page
"""


@app.route("/logout")
def logout():
    # removes user from session cookies once logged out
    flash("Ta ta for now. You have logged out.")
    session.pop("user")
    return redirect(url_for("login"))


"""
For users to create slang term and definition, adds to the database.
"""


@app.route("/add_slang", methods=["GET", "POST"])
def add_slang():
    if request.method == "POST":
        words = {
            "slang_term": request.form.get("slang_term"),
            "slang_definition": request.form.get("slang_definition"),
            "created_by": session["user"],
            # Inserts current date when slang is created
            "date_created": datetime.datetime.today().strftime('%d-%m-%y')
        }
        mongo.db.words.insert_one(words)
        flash("Slang added, cheers me ol' mucker")
        return redirect(url_for("get_words"))
    return render_template("add_slang.html")


"""
Allows users to edit only the slang entries they have created.
"""


@app.route("/edit_slang/<slang_id>", methods=["GET", "POST"])
def edit_slang(slang_id):
    if request.method == "POST":
        words = {
            "slang_term": request.form.get("slang_term"),
            "slang_definition": request.form.get("slang_definition"),
            "created_by": session["user"]
        }
        mongo.db.words.update({"_id": ObjectId(slang_id)}, words)
        flash("Slang updated, cheers me ol' mucker")

    slang = mongo.db.words.find_one({"_id": ObjectId(slang_id)})
    return render_template("edit_slang.html", slang=slang)


"""
Allows users to delete only the slang entries they have created.
"""


@app.route("/delete_slang/<slang_id>")
def delete_slang(slang_id):
    mongo.db.words.remove({"_id": ObjectId(slang_id)})
    flash("Done and dusted, slang deleted.")
    return redirect(url_for("get_words"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
