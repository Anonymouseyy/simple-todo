from flask import Flask, flash, redirect, render_template, request, session, jsonify
from jinja2.utils import markupsafe
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from deta import Base, Drive

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

base = Base("todos")


@app.route("/", methods=["GET", "POST"])
def index():
    """Home Page"""

    return render_template("index.html")