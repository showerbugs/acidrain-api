import json
import random

from django.core import serializers
from django.db.models import Model
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateTimeField
from django.db.models import IntegerField


class Sentence(Model):
    type = CharField(max_length=10)  # word, sentence
    body = TextField()
    difficulty = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @classmethod
    def random(cls, assessment_type, difficulty, count):
        all_sentences = cls.objects\
            .filter(type=assessment_type, difficulty=difficulty).all()
        return random.sample(list(all_sentences), count)

    def to_dict(self):
        serialized = serializers.serialize('json', [self])
        dicted = json.loads(serialized)[0]
        return dicted
