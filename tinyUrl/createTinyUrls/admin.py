from django.contrib import admin

# Register your models here.
from .models import TinyUrl

admin.site.register(TinyUrl)