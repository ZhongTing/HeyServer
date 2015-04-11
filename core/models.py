from django.db import models


class UserModel(models.Model):
    user_id = models.BigIntegerField(unique=True, blank=False, null=False, primary_key=True)
    access_token = models.CharField(max_length=50, default='', blank=False, unique=True)

    student_id = models.CharField(max_length=50, default='', blank=False, unique=True)

    good = models.PositiveIntegerField(default=0, blank=False, null=False)
    bad = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        db_table = "user"


class IssueModel(models.Model):
    user = models.ForeignKey(UserModel)

    actor = models.CharField(max_length=50, blank=False, null=False)
    event = models.CharField(max_length=50, blank=False, null=False)
    place = models.CharField(max_length=50, blank=True, null=False)

    latitude = models.FloatField(null=True, blank=False)
    longitude = models.FloatField(null=True, blank=False)

    good = models.PositiveIntegerField(default=0, blank=False, null=False)
    bad = models.PositiveIntegerField(default=0, blank=False, null=False)

    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "issue"