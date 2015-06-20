from django.db import models


class UserModel(models.Model):
    user_id = models.BigIntegerField(unique=True, blank=False, null=False, primary_key=True)
    access_token = models.CharField(max_length=50, default='', blank=False, unique=True)

    class Meta:
        db_table = "user"


class IssueModel(models.Model):
    user = models.ForeignKey(UserModel)
    privacy_mode = models.BooleanField(default=False, blank=False, null=False)

    subject = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=50, blank=False, null=False)
    place = models.CharField(max_length=50, blank=True, null=True)
    photo_url = models.CharField(max_length=100, blank=True, null=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    good = models.PositiveIntegerField(default=0, blank=False, null=False)

    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "issue"


class UserLikeIssuesModel(models.Model):
    user = models.ForeignKey(UserModel)
    issue = models.ForeignKey(IssueModel)

    class Meta:
        unique_together = ("user", "issue")
        db_table = "user_like_issues"
