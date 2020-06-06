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

from flask_cors import cross_origin
import json

main = Blueprint('main', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        #print(token)
        if not token:
            return jsonify({'sucess':False,'cause' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            
            current_user = User.query.filter_by(id=data['user']).first()
            
        except Exception as e:
            
            return jsonify({'sucess':False,'cause' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@main.route('/public/profile/<username>')
@cross_origin()
@token_required
def public_profile(current_user,username):
  posts = Post.query.filter_by(username=username)
  user = User.query.filter_by(name=username).first()
  if user is None:
    return jsonify({"sucess":False,
                    "cause":"Usuario nao encontrado"
                    }),400 

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

  posts_ret = [i.__dict__ for i in posts]
  [i.pop('_sa_instance_state',None) for i in posts_ret] 
  obj_ret = {
      "sucess":True,
      "posts": posts_ret,
      "user":row2dict(user),
      "user_upvotes":user_upvotes,
      "user_followers":user_followers,
      "followable":followable,
  }
  return jsonify(obj_ret)

@main.route('/private/profile')
@cross_origin()
@token_required
def private_profile(current_user):
  if current_user is None:
    return jsonify({"sucess":False,
                    "cause":"Usuario nao encontrado"
                    }),400  
  following = Follow.query.filter_by(
      follower=current_user.name)
  following = row2dict(following)
  followers = Follow.query.filter_by(
      followed=current_user.name) 
  followers = row2dict(followers)
  return jsonify({"sucess":True,
                  "followers": followers,
                  "following": following
                  }) 

@main.route('/posts')
@cross_origin()
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
  posts_ret = [i.__dict__ for i in posts]
  [i.pop('_sa_instance_state',None) for i in posts_ret]
  ret = {
      "button": button,
      "posts":posts_ret,
      "sucess":True
  }
  return jsonify(ret)


@main.route('/posts/followed')
@cross_origin()
@token_required
def posts_followed(current_user):
  posts = db.session.query(Post).join(Follow, Post.username == Follow.followed).filter(Follow.follower == current_user.name).order_by(Post.upvotes.desc()).all()
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
  posts_ret = [i.__dict__ for i in posts]
  [i.pop('_sa_instance_state',None) for i in posts_ret]
  ret = {
        "button": button,
        "posts":posts_ret,
        "sucess":True
    }
  return jsonify(ret)



@main.route('/post', methods=['POST'])
@cross_origin()
@token_required
def makepost(current_user):
    payload = json.loads(request.data)
    if payload['title'] == '' or payload['title'] is None or payload['description'] == '' or payload['description'] is None :
        return jsonify({'sucess':False, "cause":"Todos os campos são obrigatorios"}), 400

    create_post = Post(
        username=current_user.name,
        title=payload['title'],
        description=payload['description'],
        link=payload['link'])
    db.session.add(create_post)
    db.session.commit()
    return jsonify({'sucess':True})


@main.route('/deletePost/<int:id_post>', methods=['DELETE'])
@cross_origin()
@token_required
def deletePost(current_user,id_post):
  post = Post.query.filter_by(id=id_post).first()
  if post:
    if current_user.name == post.username or current_user.name == "admin1":
      db.session.delete(post)
      db.session.query(Upvote).filter(Upvote.id_post == id_post).delete()
      db.session.commit()
    else:
      return jsonify({"sucess":False,
                    "cause":"Não é possivel deletar a postagem de outro usuário"
                    }),400 
    return jsonify({'sucess':True})
  else:
    return jsonify({"sucess":False,
                    "cause":"Post nao encontrado"
                    }),400


@main.route('/editPost/<int:id_post>', methods=['PUT'])
@cross_origin()
@token_required
def editPost(current_user,id_post):
  payload = json.loads(request.data)
  post = Post.query.filter_by(id=id_post).first()
  post.title = payload['title']
  post.description = payload['description']
  post.link = payload['link']
  db.session.commit()
  return jsonify({'sucess':True})



@main.route('/follow/<username>', methods=['GET'])
@cross_origin()
@token_required
def follow(current_user,username):
  if current_user.name == username:
    return  jsonify({'sucess':False, 'cause': 'followed equal following'}),400
  followable = Follow.query.filter_by(
    follower=current_user.name, followed=username).first()

  if followable is None:
    create_follow = Follow(follower=current_user.name, followed=username)
    # deleted sqlite file, this restarted us database

    db.session.add(create_follow)
    db.session.commit()
  else:
    db.session.delete(followable)
    db.session.commit()
  return  jsonify({'sucess':True})

@main.route('/upvote/<int:id_post>', methods=['GET'])
@cross_origin()
@token_required
def upvote(current_user,id_post):
	#print(request.form['link'])
	upvotable = Upvote.query.filter_by(
	    upvoter=current_user.name, id_post=id_post).first()

	if upvotable is None:
		post = Post.query.filter_by(id=id_post).first()
		create_upvote = Upvote(id_post=id_post, upvoter=current_user.name)
		# deleted sqlite file, this restarted us database
		post.upvotes += 1
		db.session.add(create_upvote)
		db.session.commit()
	else:
		post = Post.query.filter_by(id=id_post).first()
		db.session.delete(upvotable)
		db.session.query(Upvote).filter(Upvote.id_post == id_post).delete()
		post.upvotes -= 1
		db.session.commit()
	return jsonify({'sucess':True})