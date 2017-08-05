from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sentences.models import Sentence


@admin.register(Sentence)
class SentenceAdmin(ModelAdmin):
    pass
