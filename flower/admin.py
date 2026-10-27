from django.contrib import admin
from .models import Bouquet, Order, Consultation


class TabularOrder(admin.TabularInline):
    model = Order
    extra = 1


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    list_display = ["name", "heigth", "weigth", "description", "image", "price"]
    inlines = [TabularOrder]
