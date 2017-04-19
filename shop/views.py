from django.shortcuts import render
from .models import ShopItem, ShopCategory
from django.db.models import Q
from django.utils import timezone


def shop_list(request):
	tags = ShopCategory.objects.all()
	items = ShopItem.objects.all()
	last_items = ShopItem.objects.all()[:3]
	query = request.GET.get('q')
	if query :
		items = ShopItem.objects.filter(
            category__name__startswith=query 
           	).order_by('-published')
	context = {
	  'last_items':last_items,
	  'items':items,
	  'tags':tags,
	}
	return render (request,'shop/shop_list.html',context)
