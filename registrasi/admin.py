from django.contrib import admin

# Register your models here.
from registrasi.models import Supplier, Material

admin.site.register(Supplier)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'type', 'buy_price', 'supplier']
    list_filter = ['type']
    search_fields = ['code', 'name']


admin.site.register(Material, MaterialAdmin)
