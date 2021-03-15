from django.contrib import admin

from suppliers import models

@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created', 'modified')
