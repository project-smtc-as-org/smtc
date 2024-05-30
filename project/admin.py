from django.contrib import admin

from . import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'description')


@admin.register(models.CodeType)
class CodeTypeAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')


@admin.register(models.Code)
class CodeAdmin(admin.ModelAdmin):
  list_display = ('id', 'type', 'code', 'source', 'name', 'created_at')
