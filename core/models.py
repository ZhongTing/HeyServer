from django.db import models


class CouponModel(models.Model):
    coupon_code = models.CharField(max_length=20, unique=True, blank=False, null=False)
    used = models.BooleanField(default=False, null=False)

    class Meta:
        db_table = "coupon"


class UserModel(models.Model):
    user_id = models.BigIntegerField(unique=True, blank=False, null=False, primary_key=True)
    access_token = models.CharField(max_length=50, blank=False, null=False, unique=True)

    device_identity = models.CharField(max_length=50, blank=False, null=False)

    notification_token = models.CharField(max_length=180, default='')

    class Meta:
        db_table = "user"


class UserIssueFiltersModel(models.Model):
    user = models.ForeignKey(UserModel)
    subject = models.CharField(max_length=20, blank=False, null=False)
    enable = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        db_table = "user_issue_filters"
        unique_together = ("user", "subject")


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
