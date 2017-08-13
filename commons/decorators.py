from functools import wraps
import json
from json.decoder import JSONDecodeError

from django.http import JsonResponse


def validate_request_body(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        request = args[0]
        body = request.body.decode()

        try:
            body = json.loads(body)
        except JSONDecodeError:
            return JsonResponse(
                status=400,
                data={
                    'message': 'wrong json format',
                }
            )

        if not body:
            return JsonResponse(
                status=400,
                data={
                    'message': 'no request body',
                }
            )

        request.json = body
        return f(request, **kwargs)

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
