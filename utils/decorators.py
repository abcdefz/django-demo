import json
import time
from functools import wraps
from RBAC.models import User
from .errors import forbidden, bad_request

TOKEN = "RBAC_TOKEN"

def json_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            body = json.loads(request.body.decode("utf8"))
        except Exception as e:
            return bad_request(str(e))

        if not body:
            return bad_request('Body is Empty.')

        kwargs['body'] = body
        return func(request, *args, **kwargs)

    return wrapper


def login_required(func):
    @wraps(func)
    def decorated_function(request, *args, **kwargs):
        authorization = request.META.get(f'HTTP_{TOKEN}')
        if not authorization:
            return forbidden('Unkown Token')
        user = User.verify_auth_token(authorization)
        if not user:
            return forbidden('Unknown Token')
        kwargs['user'] = user
        return func(request, *args, **kwargs)

    return decorated_function


def permission_required(permission):
    def outer_wrapper(func):
        def inner_wrapper(request, *args, **kwargs):
            user = kwargs['user']
            if not user.verify_permission(permission):
                return forbidden('Forbidden Permission')
            return func(request, *args, **kwargs)
        return inner_wrapper
    return outer_wrapper


def test(name):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print(f'-- name -- {name}')
            result = func(*args, **kwargs)
            return result
        return inner_wrapper
    return outer_wrapper