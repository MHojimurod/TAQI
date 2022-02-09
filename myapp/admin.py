from django.contrib import admin

# Register your models here.
from myapp.models import News,NewsCategory
admin.site.register(NewsCategory)
admin.site.register(News)