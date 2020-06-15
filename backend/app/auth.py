from flask import Blueprint, render_template, redirect, url_for, request, flash,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required,current_user
import json
import jwt
import datetime
from flask import current_app as app
from .models import User
from . import db
from .utils import  row2dict
from flask_cors import cross_origin

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login_post():

    payload = json.loads(request.data)
    if  payload['password']  is None or payload['email'] is None:
        return jsonify({
        
        "sucess":False,
        "cause":"Por favor verifique seu usuário e senha"
        }), 400
    email = payload['email']
    password = str(payload['password'])

    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, password):
        return jsonify({
                "sucess":False,
                "cause":"Por favor verifique seu usuário e senha"
                }),400

    token = jwt.encode({"user":user.id,"exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=300)}, app.config['SECRET_KEY'])

    return  jsonify({
                "user":row2dict(user),
                "sucess":True,
                "token":token.decode('UTF-8'),
                "cause":"Your log in on"
                }), 200


@auth.route('/signup', methods=['POST'])
@cross_origin()
def signup_post():

    payload = json.loads(request.data)
    if  payload['password']  is None or payload['password']  == "":
        return jsonify({
        "sucess":False,
        "cause":"A senha não pode ser vazia"
        }), 400

    if  payload['email']  is None or payload['email']  == "":
        return jsonify({
        "sucess":False,
        "cause":"O email não pode ser vazio"
        }), 400

    if  payload['name']  is None or payload['name']  == "":
        return jsonify({ 
        "sucess":False,
        "cause":"O nome não pode ser vazio"
       }), 400
       
    email = payload['email']
    name = payload['name']
    password = str(payload['password'])

    user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({"success":False, "cause":"Email address already exists."}), 400

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"success":True})

