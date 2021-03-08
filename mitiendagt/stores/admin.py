from django.contrib import admin

from stores.models import Store
# Register your models here.

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """Store admin."""

    list_display = ('id', 'name', 'address', 'phone')
    search_fields = ('name',)
    list_filter = ('created', 'modified')
