import json

from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic import View


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

        user = User.objects.create_user(name, password=password)
        user = json.loads(serializers.serialize('json', [user]))[0]
        print(user)
        serialized_user = {
            'name': user['fields']['username'],
            'joined_at': user['fields']['date_joined'],
            'last_signin_at': user['fields']['last_login'],
        }

        return JsonResponse({
            'success': True,
            'user': serialized_user,
        })


class SessionView(View):
    def post(self, request):
        pass
