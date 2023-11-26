from flask import Flask, render_template, Blueprint
from views.index import Index
from views.login import Login

app = Flask(__name__)

app.register_blueprint(Index)
app.register_blueprint(Login)


if __name__ == "__main__":
    app.run(debug=True)