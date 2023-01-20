from http.client import CannotSendRequest
from wsgiref.validate import validator
from flask import Blueprint, current_app, render_template, send_file, request, redirect, url_for, flash, session
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/")
def home_page():
    return render_template("home_page.html")
        