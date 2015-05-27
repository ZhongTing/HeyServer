from core.issue.issue import Issue
from rest_framework import serializers


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = (
            'user',
            'subject',
            'description',
            'place',
            'latitude',
            'longitude',
        )