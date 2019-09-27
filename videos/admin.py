from django.contrib import admin
from videos.models import Video

# Register your models here.
# Allows you to access database through the Admin page.
admin.site.register(Video)