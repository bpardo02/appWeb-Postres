from django.contrib import admin
from .models import Flan, ContactForm


@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ("name", "flan_uuid", "slug", "is_private")
    search_fields = ("name", "description", "slug")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ContactForm)
