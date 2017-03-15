from django.shortcuts import render
from .models import ShopItem, ShopCategory

def shop_list(request):
	items = ShopItem.objects.all()
	context = {
	  'items':items,
	}
	return render (request,'shop/shop_list.html',context)
