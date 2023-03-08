from django.contrib import admin

# Register your models here.
from .models import Task, Status, Slot

admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Slot)
