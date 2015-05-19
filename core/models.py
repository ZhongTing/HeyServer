from django.db import models


class UserModel(models.Model):
    user_id = models.BigIntegerField(unique=True, blank=False, null=False, primary_key=True)
    access_token = models.CharField(max_length=50, default='', blank=False, unique=True)

    student_id = models.CharField(max_length=50, default='', blank=False, unique=True)

    good = models.PositiveIntegerField(default=0, blank=False, null=False)
    bad = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        db_table = "user"


class Subject(models.Model):
    subject_id = models.BigIntegerField(unique=True, blank=False, null=False, primary_key=True)
    content = models.CharField(max_length=50, blank=False, null=False, unique=True)
    count = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        db_table = "subject"


class Description(models.Model):
    subject_id = models.ForeignKey("Subject")
    description_id = models.BigIntegerField(unique=True, blank=False, null=False, primary_key=True)
    content = models.CharField(max_length=50, blank=False, null=False, unique=True)
    count = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        db_table = "description"


class Place(models.Model):
    subject_id = models.ForeignKey("Subject")
    place_id = models.BigIntegerField(unique=True, blank=False, null=False, primary_key=True)
    content = models.CharField(max_length=50, blank=False, null=False, unique=True)
    count = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        db_table = "place"


class IssueModel(models.Model):
    user = models.ForeignKey(UserModel)

    subject = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=50, blank=False, null=False)
    place = models.CharField(max_length=50, blank=True, null=True)
    image_filename = models.CharField(max_length=100, blank=True, null=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    good = models.PositiveIntegerField(default=0, blank=False, null=False)

    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "issue"