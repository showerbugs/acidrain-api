import json

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.core import serializers
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator

from commons.decorators import request_body_required
from commons.decorators import login_required
from users.models import User


@method_decorator(request_body_required, name='dispatch')
class UserView(View):
    def post(self, request):
        if not request.body:
            return JsonResponse({
                'success': False,
                'message': 'no request body',
            })

        params = json.loads(request.body.decode())
        name = params.get('name')
        password = params.get('password')
        if not name or not password:
            return JsonResponse({
                'success': False,
                'message': 'no name or password',
            })

        try:
            user = User.objects.create_user(name, password=password)
        except IntegrityError:
            return JsonResponse({
                'success': False,
                'message': 'this name already exists',
            })
        user = user.to_dict()

        return JsonResponse({
            'success': True,
            'user': {
                'name': user['fields']['username'],
                'joined_at': user['fields']['date_joined'],
            },
        })


class SessionView(View):
    @method_decorator(request_body_required)
    def post(self, request):
        params = json.loads(request.body.decode())
        name = params.get('name')
        password = params.get('password')
        if not name or not password:
            return JsonResponse({
                'success': False,
                'message': 'no name or password',
            })

        user = authenticate(username=name, password=password)
        if not user:
            return JsonResponse({
                'success': False,
                'message': 'authentication failed',
            })
        login(request, user)

        serialized = serializers.serialize('json', [user])
        user = json.loads(serialized)[0]

        return JsonResponse({
            'success': True,
            'user': {
                'name': user['fields']['username'],
                'joined_at': user['fields']['date_joined'],
                'last_signin_at': user['fields']['last_login']
            },
        })

    # @method_decorator(login_required)
    def delete(self, request):
        # logout(request)

        return JsonResponse({
            'success': True,
        })
