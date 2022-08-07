from django.contrib import admin

# Register your models here.
from .models import list_of_executed, RegisteredUsers, Employees


admin.site.register(list_of_executed)
admin.site.register(RegisteredUsers)
admin.site.register(Employees)
