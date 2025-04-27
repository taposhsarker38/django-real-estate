from django.contrib import admin

from .models import Enquiry


# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "email", "message"]


admin.site.register(Enquiry, EnquiryAdmin)
