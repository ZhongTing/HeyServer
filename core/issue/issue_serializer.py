from core.models import IssueModel
from rest_framework import serializers


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueModel
        fields = (
            'user',
            'actor',
            'event',
            'place',
            'latitude',
            'longitude',
        )