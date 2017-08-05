from functools import wraps

from django.http import JsonResponse


def request_body_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        request = args[0]
        if not request.body:
            return JsonResponse({
                'success': False,
                'message': 'no request body',
            })
        return f(*args, **kwargs)

    return wrap


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        request = args[0]
        if not request.user.is_authenticated():
            return JsonResponse({
                'success': False,
                'message': 'login required',
            })
        return f(*args, **kwargs)

    return wrap
