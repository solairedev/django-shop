from django.db import models
from django.utils import timezone 

def upload_img(object,filename):
	return 'image/%s/%s'%(object.slug,filename)

class ShopCategory(models.Model):
	name = models.TextField(verbose_name="Наименование")
	slug = models.SlugField(max_length=200,verbose_name="Ссылка",blank=True, null=True)

	class Meta:
		verbose_name = ('Категория')
		verbose_name_plural = ('Категории')

	def __str__(self):
		return self.name

class ShopItem(models.Model):
	name = models.CharField(max_length=100,verbose_name="Наименование")
	description = models.TextField(verbose_name="Описание")
	price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True, verbose_name="Цена")
	category = models.ForeignKey(ShopCategory,verbose_name="Категория",blank=True, null=True)
	slug = models.SlugField(max_length=200,verbose_name="Ссылка",blank=True, null=True)
	img = models.FileField(upload_to=upload_img,blank=True, null=True,verbose_name="Изображение")
	stock = models.PositiveIntegerField(blank=True, null=True,verbose_name="Количество")
	available = models.BooleanField(default=True,verbose_name="Доступность")
	published = models.DateTimeField(verbose_name="Дата добавления",default=timezone.now)
	updated = models.DateTimeField(verbose_name="Дата изменения",default=timezone.now)



	class Meta:
		verbose_name = ('Товар')
		verbose_name_plural = ('Товары')
		ordering = ['-published']

	def __str__(self):
		return self.name