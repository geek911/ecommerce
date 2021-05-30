from django.contrib import admin
from .models import *

admin.site.site_header = 'uMall Administrator'  # default: "Django Administration"
admin.site.index_title = 'Features Area'  # default: "Site administration"
admin.site.site_title = 'uMall | Administrator'  # default: "Django site admin"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "quantity", "price")


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
