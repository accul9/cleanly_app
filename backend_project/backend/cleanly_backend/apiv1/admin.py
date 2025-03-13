from django.contrib import admin
from .views.models.models import Task
from .views.models.models import CustomUser

# Register your models here.
admin.site.register(Task)
admin.site.register(CustomUser)

