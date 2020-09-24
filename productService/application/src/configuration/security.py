
import jwt
import constant.security as SEC
import time

def generate(claims={}, seconds=1000):
    claims['exp'] = int(time.time()+seconds)
    token = jwt.encode(claims, SEC.KEY, algorithm= SEC.ALGORITHM)
    return token

def validate(token):
    result = False
    try:
        result = jwt.decode(token, SEC.KEY, algorithm= SEC.ALGORITHM)
    except jwt.InvalidSignatureError:
        print("Incorrect token key")
    except jwt.ExpiredSignatureError:
        print("Token expired")
    except jwt.InvalidTokenError:
        print("Undecodable token")
    return result