from django.contrib import admin
from .models import Movie

# Register your models here.
# For admin to be able to edit data
admin.site.register(Movie)
