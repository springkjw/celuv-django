from django.contrib import admin

from .models import Celebrity


class CelebrityAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    autocomplete_fields = ['entertainment']


admin.site.register(Celebrity, CelebrityAdmin)
