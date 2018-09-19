from django.contrib import admin

# Register your models here.

from app.models.articles import Articles

admin.site.register(Articles)
