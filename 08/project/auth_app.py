from flask import Blueprint, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)

from .models import User, db


auth = Blueprint("auth", __name__, url_prefix='/api/v1/auth')


@auth.post('/register')
def register():
    username = request.json.get('username', '')
    email = request.json.get('email', '')
    password = request.json.get('password', '')

    # walidacje ...
    if len(password) < 5:
        return {
            "error": "Password is too short"
        }, 400

    if User.query.filter(User.email==email).first() is not None:
        return {
            "error": "Email is taken"
        }, 400

    pwd_hash = generate_password_hash(password)
    user = User(
        username=username,
        password=pwd_hash,
        email=email
    )
    db.session.add(user)
    db.session.commit()

    return {
        "msg": "User created",
        "user": {
            "username": username,
            "email": email
        }
    }

@auth.post('/login')
def login():
    email = request.json.get('email', '')
    password = request.json.get('password', '')

    user = User.query.filter(User.email == email).first()
    if user:
        is_pass_correct = check_password_hash(user.password, password)
        if is_pass_correct:
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)

            return {
                "user": {
                    "refresh":  refresh,
                    "access": access,
                    "username": user.username,
                    "email": user.email
                }
            }

    return {
        "error": "Wrong credentials"
    }, 401
