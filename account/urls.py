from django.urls import path, include

from . import views


urlpatterns = [
  path("", views.index, name="account-index"),
  path("register/", views.register, name="account-register"),
  path("login/", views.login, name="account-login"),
  path("logout/", views.logout, name="account-logout"),
]
