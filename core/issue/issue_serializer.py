from core.models import IssueModel
from rest_framework import serializers


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueModel
        fields = (
            'user',
            'subject',
            'description',
            'place',
            'latitude',
            'longitude',
        )