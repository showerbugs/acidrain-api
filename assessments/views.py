import json

from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator

from commons.decorators import request_body_required
from commons.decorators import login_required
from assessments.models import Assessment
from assessments.models import History


@method_decorator(request_body_required, name='dispatch')
class HistoryView(View):
    # @method_decorator(login_required)
    def post(self, request):
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
