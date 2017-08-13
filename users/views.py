import json

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.core import serializers
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator

from commons.decorators import validate_request_body
from commons.decorators import login_required
from users.models import User


@method_decorator(validate_request_body, name='dispatch')
class UserView(View):
    def post(self, request):
        name = request.json.get('name')
        password = request.json.get('password')
        if not name or not password:
            return JsonResponse(
                status=400,
                data={
                    'success': False,
                    'message': 'no name or password',
                }
            )

        try:
            user = User.objects.create_user(name, password=password)
        except IntegrityError:
            return JsonResponse(
                status=409,
                data={
                    'message': 'already existed name',
                }
            )
        user = user.to_dict()

        return JsonResponse(
            status=201,
            data={
                'user': {
                    'id': user['pk'],
                    'name': user['fields']['username'],
                    'joined_at': user['fields']['date_joined'],
                },
            }
        )


class SessionView(View):
    @method_decorator(validate_request_body)
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

    @method_decorator(login_required)
    def delete(self, request):
        logout(request)

        return JsonResponse({
            'success': True,
        })
