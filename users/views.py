import json

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.core import serializers
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.views.generic import View

from users.models import User


class UserView(View):
    def post(self, request):
        if not request.body:
            return JsonResponse({
                'success': False,
                'message': 'no request body',
            })

        params = json.loads(request.body)
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
    def post(self, request):
        if not request.body:
            return JsonResponse({
                'success': False,
                'message': 'no request body',
            })

        params = json.loads(request.body)
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

    def delete(self, request):
        if not request.user.is_authenticated():
            return JsonResponse({
                'success': False,
                'message': 'login required',
            })
        logout(request)

        return JsonResponse({
            'success': True,
        })
