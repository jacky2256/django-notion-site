from django.contrib import admin
from notion_app.models import ExampleModel

@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    pass
