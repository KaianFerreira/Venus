from flask import Blueprint,Flask, request, jsonify, make_response,url_for
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
import datetime
from functools import wraps
from .models import Post, Upvote, User, Follow
from . import db
from .utils import extract, row2dict
from .auth import jwt
from flask import current_app as app
import json

main = Blueprint('main', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        #print(token)
        if not token:
            return jsonify({'Sucess':False,'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            
            current_user = User.query.filter_by(id=data['user']).first()
            
        except Exception as e:
            
            return jsonify({'Sucess':False,'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


def get_all_users(current_user):

    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)

    return jsonify({'users' : output})

@main.route('/public/profile/<username>')
@token_required
def public_profile(current_user,username):
  print(username)
  posts = Post.query.filter_by(username=username)
  user = User.query.filter_by(name=username).first()
  if user is None:
    return jsonify({"Sucess":False})


  my_upvotes = db.session.query(Upvote.id_post).filter(Upvote.upvoter == current_user.name).all()
  my_upvotes = extract(my_upvotes)
  if posts:
    for post in posts:
      if post.id in my_upvotes:
        post.upvote = 'Downvote'
      else:
        post.upvote = 'Upvote'

  followable = Follow.query.filter_by(
      follower=current_user.name, followed=username).first()
  if followable is None:
    followable_style = 'is-info'
    followable = 'Follow'
  else:
    followable_style = 'is-danger'
    followable = 'Unfollow'

  user_upvotes = db.session.query(func.sum(
      Post.upvotes)).filter(Post.username == username).one()[0]
  user_followers = db.session.query(func.count(
      Follow.follower)).filter(Follow.followed == username).one()[0]
  if user_upvotes is None:
    user_upvotes = 0
  obj_ret = {
      "Sucess":True,
      "posts": [row2dict(i) for i in posts],
      "user":row2dict(user),
      "user_upvotes":user_upvotes,
      "user_followers":user_followers,
      "followable":followable,
  }
  return jsonify(obj_ret)

@main.route('/posts')
@token_required
def posts(current_user):
  posts = Post.query.order_by(Post.upvotes.desc()).all()
  my_upvotes = db.session.query(Upvote.id_post).filter(Upvote.upvoter == current_user.name).all()
  my_upvotes = extract(my_upvotes)
  button = {'text':'Veja somente pessoas que você segue', 'url': url_for('main.posts') }
  if posts:
    for post in posts:
      if post.id in my_upvotes:
        post.upvote = 'Downvote'
      else:
        post.upvote = 'Upvote'
   
    error = None
  else:
    error = 'You don\'t have any content.'
  posts_ret = [row2dict(i) for i in posts]
  ret = {
      "button": button,
      "posts":posts_ret,
      "Sucess":True
  }
  return jsonify(ret)


@main.route('/post', methods=['POST'])
@token_required
def makepost(current_user):
    payload = json.loads(request.data)
    if payload['title'] == '' or payload['description'] == '':
        return {'Sucess':False} 

    create_post = Post(
        username=current_user.name.decode("utf-8"),
        title=payload['title'],
        description=payload['description'],
        link=payload['link'])
    db.session.add(create_post)
    db.session.commit()
    return {'Sucess':True}