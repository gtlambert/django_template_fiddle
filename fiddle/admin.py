from django.contrib import admin

from .models import Fiddle

class FiddleAdmin(admin.ModelAdmin):
    list_display = ['id', 'context', 'template']


admin.site.register(Fiddle, FiddleAdmin)
