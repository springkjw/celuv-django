from django.contrib import admin

from .models import Entertainment, Manager


class EntertainmentAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Entertainment, EntertainmentAdmin)
admin.site.register(Manager)
