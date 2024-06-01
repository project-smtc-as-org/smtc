""" Project :: Project and Issue
"""
from functools import partial

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from smtc.utils import redirect_to_app_index, strip_form_values
from . import models


redirect_to_app_index = partial(redirect_to_app_index, 'project-index')


@login_required
@require_http_methods(["GET"])
def index(request, code: int | None = None):
  """ Index page: Created projects/issues by others
  """
  # TODO:
  # pagination
  # filters: Tags, Topics
  # search: by name
  if code:
    code = models.Code.objects.filter(id=code_id).all()
    code = None if not code else code.pop()

  return render(
    request,
    'project/index.html',
    {
      'code': code
      'codes': models.Code.objects.all().exclude(created_by=request.user),
      'tags': models.Tag.objects.all(),
    }
  )
