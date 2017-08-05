import json

from django.http import JsonResponse
from django.views.generic import View

from sentences.models import Sentence


class SentenceView(View):
    def get(self, request):
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
        sentence_count = params.get('sentence_count')
        if not assessment_type or not difficulty or not sentence_count:
            return JsonResponse({
                'success': False,
                'message': 'assessment_type, difficulty, sentence_count are required',
            })
        difficulty = int(difficulty)
        sentence_count = int(sentence_count)

        try:
            samples = Sentence.random(
                assessment_type, difficulty, sentence_count)
        except ValueError:
            return JsonResponse({
                'success': False,
                'message': 'sentences are not enough',
            })

        sentences = []
        for sample in samples:
            sample = sample.to_dict()
            sentences.append({
                'body': sample['fields']['body'],
                'difficulty': sample['fields']['difficulty'],
                'type': sample['fields']['type'],
            })

        return JsonResponse({
            'success': True,
            'sentences': sentences,
        })
