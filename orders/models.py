from django.db import models
from shop.models import ShopItem

class Order(models.Model):
	first_name = models.CharField(max_length=50,verbose_name="Имя")
	last_name = models.CharField(max_length=50,verbose_name="Фамилия")
	email = models.EmailField(verbose_name="Почта")
	address = models.CharField(max_length=250,verbose_name="Адрес")
	postal_code = models.CharField(max_length=20,verbose_name="Индекс")
	city = models.CharField(max_length=100,verbose_name="Город")
	created = models.DateTimeField(auto_now_add=True,verbose_name="Дата создания")
	updated = models.DateTimeField(auto_now=True,verbose_name="Дата изменения")
	paid = models.BooleanField(default=False,verbose_name="Оплачено")
	
	class Meta:
		verbose_name = ('Заказ')
		verbose_name_plural = ('Заказы')
		ordering = ('-created',)
	
	def __str__(self):
		return 'Order {}'.format(self.id)
	
	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items')
	product = models.ForeignKey(ShopItem, related_name='order_items')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)
	
	def __str__(self):
		return '{}'.format(self.id)
	
	def get_cost(self):
		return self.price * self.quantity