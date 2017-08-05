import json

from django.contrib.auth.models import User as DefaultUser
from django.core import serializers


class User(DefaultUser):
    class Meta:
        proxy = True

    def to_dict(self):
        serialized = serializers.serialize('json', [self])
        dicted = json.loads(serialized)[0]
        return dicted
