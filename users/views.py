import json

from django.contrib.auth.models import User
from django.core import serializers
from django.db.utils import IntegrityError
from django.http import JsonResponse
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

        try:
            user = User.objects.create_user(name, password=password)
        except IntegrityError:
            return JsonResponse({
                'success': False,
                'message': 'this name already exists',
            })
        user = json.loads(serializers.serialize('json', [user]))[0]

        return JsonResponse({
            'success': True,
            'user': {
                'name': user['fields']['username'],
                'joined_at': user['fields']['date_joined'],
            },
        })


class SessionView(View):
    def post(self, request):
        pass
