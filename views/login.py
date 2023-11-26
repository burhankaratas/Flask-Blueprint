from flask import Flask, render_template, Blueprint

Login = Blueprint("Login", __name__, template_folder="templates")

@Login.route("/login")
def index():
    return render_template("login.html")