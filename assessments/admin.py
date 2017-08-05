from django.contrib import admin
from django.contrib.admin import ModelAdmin

from assessments.models import Assessment
from assessments.models import History


@admin.register(Assessment)
class AssessmentAdmin(ModelAdmin):
    pass


@admin.register(History)
class HistoryAdmin(ModelAdmin):
    pass
