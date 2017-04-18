from django.contrib import admin
from shop.models import ShopItem,ShopCategory

class ShopCategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	search_fields = ['name','slug']
	list_per_page = 10

admin.site.register(ShopCategory,ShopCategoryAdmin)

class ShopItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock',
 'available', 'published', 'updated']
    list_filter = ['available','published','updated']
    list_editable = ['price','stock','available']
    search_fields = ['name','slug','description']
    list_per_page = 10


admin.site.register(ShopItem,ShopItemAdmin)


