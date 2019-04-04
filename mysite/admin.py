from django.contrib import admin

# Register your models here.

from .models import contact,students

admin.site.register(students)

admin.site.register(contact)
