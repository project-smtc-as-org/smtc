from django.urls import path, include
# from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path("", views.index, name="realm-index"),
  path("register/", views.register, name="realm-register"),
  path("login/", views.login, name="realm-login"),
  path("logout/", views.logout, name="realm-logout"),
]
