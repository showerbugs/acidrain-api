from django.db.models import Model
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import DateTimeField
from django.db.models import IntegerField


class Assessment(Model):
    type = CharField(max_length=10)  # word, sentence
    total = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class History(Model):
    user = ForeignKey('auth.User', related_name='assessment_histories')
    assessment = ForeignKey('Assessment', related_name='histories')
    score = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
