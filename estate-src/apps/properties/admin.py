from django.contrib import admin

from .models import Property, PropertyViews


# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "property_type",
        "advert_type",
        "country",
    )
    list_filter = ("property_type", "advert_type", "country")


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyViews)
