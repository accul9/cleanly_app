from django.contrib import admin
from .models.models import Task
from .models.t_user import CustomUser

# Register your models here.
admin.site.register(Task)
admin.site.register(CustomUser)

