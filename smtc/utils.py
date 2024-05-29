from django.http import HttpResponseRedirect
from django.urls import reverse


def redirect_to_app_index(index_page, request):
  """ Redirect to the application index page
  """
  return HttpResponseRedirect(reverse(index_page))


def strip_form_values(kwargs):
  """ Uses `.strip() or None` for str values
  """
  new_kwargs = {}
  for key, value in kwargs.items():
    if not isinstance(value, str):
      continue
    new_kwargs[key] = value.strip() or None
  return new_kwargs
