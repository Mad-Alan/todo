from django.contrib import admin
from .models import ToDo
from .models import library

admin.site.register(ToDo)
admin.site.register(library)

