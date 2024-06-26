""" Account :: Authentication
"""
from functools import partial

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from smtc.utils import redirect_to_app_index, strip_form_values

from . import forms


redirect_to_app_index = partial(redirect_to_app_index, 'account-index')


@login_required
@require_http_methods(["GET"])
def index(request):
  """ Index page
  """
  return render(
    request,
    'account/index.html',
    {
    }
  )


@require_http_methods(["GET", "POST"])
def register(request):
  if request.method == "POST":
    form = forms.UserForm(request.POST)
    form_data = strip_form_values(form.data)
    username = form_data.get("username")
    password = form_data.get("password")
    if all((username, password)):
      user = User.objects.filter(username=username)
      if not user.exists():
        user = User.objects.create_user(username=username, password=password)
        return redirect(login)
  else:
    form = forms.UserForm(request.POST)

  return render(
    request,
    'account/register.html',
    {
      "form": form,
      "al_register": True,
    }
  )


@require_http_methods(["GET", "POST"])
def login(request):
  """ Login page
  """
  if request.user.is_authenticated:
    auth_logout(request)

  if request.method == "POST":
    form = forms.UserForm(request.POST)
    form_data = strip_form_values(form.data)
    username = form_data.get("username")
    password = form_data.get("password")
    if all((username, password)):
      user = authenticate(username=username, password=password)
      if user is not None:
        auth_login(request, user)
        next_page = request.POST.get("next")
        if next_page:
          return redirect(next_page)
        return redirect_to_app_index(request)
      # FIXFOR: `A user with that username already exists.`
      form.errors.clear()
      form.add_error("username", ["Credentials are not valid"])
  else:
    form = forms.UserForm()

  return render(
    request,
    'account/login.html',
    {
      "form": form,
      "al_login": True
    }
  )


@login_required
@require_http_methods(["GET"])
def logout(request):
  """ Logout page
  """
  auth_logout(request)
  return redirect(login)
