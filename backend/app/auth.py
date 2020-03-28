from flask import Blueprint, render_template, redirect, url_for, request, flash,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required,current_user
import json
import jwt
import datetime
from flask import current_app as app
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login_post():

    payload = json.loads(request.data)
    email = payload['email'].encode("utf-8")
    password = str(payload['password'])

    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, password):
        return jsonify({
                "Sucess":False,
                "Cause":"Please check your login details and try again."
                })

    token = jwt.encode({"user":email.decode('utf-8'),"exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

    return  jsonify({
                "Sucess":True,
                "Token":token.decode('UTF-8'),
                "Cause":"Your log in on"
                })

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    payload = json.loads(request.data)
    email = payload['email'].encode("utf-8")
    name = payload['name'].encode("utf-8")
    password = str(payload['password'])

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return jsonify({"Success":False})

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"Success":True})

