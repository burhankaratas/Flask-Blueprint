from flask import Flask, render_template, Blueprint

Index = Blueprint("Index", __name__, template_folder="templates")

@Index.route("/")
def index():
    return render_template("index.html")