from django.contrib import admin

# Register your models here.

from .models import voluntary_video, mandatory_video


admin.site.register(voluntary_video)
admin.site.register(mandatory_video)