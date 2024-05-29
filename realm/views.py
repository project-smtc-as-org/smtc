""" Realm (Autherization)
"""
from functools import partial

from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from sh1chan.utils import redirect_to_app_index

from . import forms


# NOTE: redirecting to the project index
redirect_to_app_index = partial(redirect_to_app_index, 'index-index')


@login_required
def index(request):
  """ Index page, list of sessions, session manipulation
  """
  return HttpResponse('<h1>Index</h1>')


def register(request):
  if request.method == "POST":
    form = forms.UserForm(request.POST)
    username = form.data["username"]
    password = form.data["password"]
    if all((username, password)):
      user = User.objects.filter(username=username)
      if not user.exists():
        user = User.objects.create_user(username=username, password=password)
        return redirect(login)
  else:
    form = forms.UserForm(request.POST)

  return render(
    request,
    'realm/register.html',
    {
      "form": form
    }
  )


def login(request):
  """ Login page
  """
  session_user = request.user
  if session_user and session_user.is_authenticated:
    auth_logout(request)

  if request.method == "POST":
    form = forms.UserForm(request.POST)
    username = form.data["username"]
    password = form.data["password"]
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
    'realm/login.html',
    {
      "form": form
    }
  )


@login_required
def logout(request):
  """ Logout page
  """
  auth_logout(request)
  return redirect(login)
