import uuid
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
  """ Tag Model: Programming Language and NoN Programming Language
  """
  class Meta:
    db_table = 'thecode__tag'

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50, blank=False, null=False)
  description = models.TextField(blank=False, null=False)

  def __str__(self):
    return self.name


class Topic(models.Model):
  """ Topic Model
  """
  class Meta:
    db_table = 'thecode__topic'

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50, blank=False, null=False)
  description = models.TextField(blank=False, null=False)

  def __str__(self):
    return self.name


class CodeType(models.Model):
  """ CodeType Model: project and issue
  """
  class Meta:
    db_table = 'thecode__code_type'

  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, blank=False, null=False)

  def __str__(self):
    return self.name


class Code(models.Model):
  """ Code Model: Basic info about the Code and a *source to it
  """
  class Meta:
    db_table = 'thecode__code'

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  type = models.ForeignKey(
    CodeType,
    blank=False, null=True,
    on_delete=models.SET_NULL
  )
  code = models.ForeignKey(
    "Code",
    blank=True, null=True,
    on_delete=models.SET_NULL, related_name='branch'
  )
  source = models.CharField(max_length=100, blank=False, null=False)
  name = models.CharField(max_length=50, blank=False, null=False)
  description = models.TextField(blank=False, null=False)
  created_by = models.ForeignKey(
    User,
    blank=True, null=True,
    on_delete=models.SET_NULL, related_name='code_created'
  )
  follower = models.ManyToManyField(
    User,
    blank=True,
    related_name='code_followed'
  )
  tag = models.ManyToManyField(Tag)
  topic = models.ManyToManyField(Topic)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

