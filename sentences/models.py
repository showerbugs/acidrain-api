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
