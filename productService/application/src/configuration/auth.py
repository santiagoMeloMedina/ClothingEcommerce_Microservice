
from functools import wraps
from flask import jsonify, request
import constant.auth as AUTH
from model.response import Response
from configuration.security import validate

def system(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        result = jsonify(Response(403, AUTH.REJECTED).toMap())
        token = dict(request.headers)["Sauthentication"]
        data = validate(token)
        if data:
            verify = AUTH.ROLE["SYSTEM"].issubset(set(data["roles"]))
            if verify:
                result = func(*args, **kargs)
        return result
    return wrapper

def user(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        result = jsonify(Response(403, AUTH.REJECTED).toMap())
        token = dict(request.headers)["Authentication"]
        data = validate(token)
        if data:
            verify = AUTH.ROLE["USER"].issubset(set(data["roles"]))
            if verify:
                result = func(*args, **kargs)
        return result
    return wrapper

def admin(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        result = jsonify(Response(403, AUTH.REJECTED).toMap())
        token = dict(request.headers)["Authentication"]
        data = validate(token)
        if data:
            verify = AUTH.ROLE["ADMIN"].issubset(set(data["roles"]))
            if verify:
                result = func(*args, **kargs)
        return result
    return wrapper





