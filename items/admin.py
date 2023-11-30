from django.contrib import admin

from items.models import Item

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'currency')
    fields = ('name', 'description', 'price', 'currency', 'stripe_item_price_id')

