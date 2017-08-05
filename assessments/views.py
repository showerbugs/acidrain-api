import json

from django.http import JsonResponse
from django.views.generic import View

from assessments.models import Assessment
from assessments.models import History


class HistoryView(View):
    def post(self, request):
        if not request.body:
            return JsonResponse({
                'success': False,
                'message': 'no request body',
            })

        # if not request.user.is_authenticated():
        #     return JsonResponse({
        #         'success': False,
        #         'message': 'login required',
        #     })

        params = json.loads(request.body.decode())
        assessment_type = params.get('assessment_type')
        difficulty = params.get('difficulty')
        score = params.get('score')
        if not assessment_type or not difficulty or not score:
            return JsonResponse({
                'success': False,
                'message': 'assessment_type, difficulty, score are required',
            })
        difficulty = int(difficulty)
        score = int(score)

        History.objects.create(**{
            'user': request.user,
            'assessment': Assessment.objects.get(type=assessment_type),
            'score': score,
        })

        return JsonResponse({
            'success': True,
        })
