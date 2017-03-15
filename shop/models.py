from django.db import models
from django.utils import timezone 

def upload_img(object,filename):
	return '/image/%s/%s'%(object.name,filename)

class ShopCategory(models.Model):
	name = models.TextField(verbose_name="Наименование")

	class Meta:
		verbose_name = ('Категория')
		verbose_name_plural = ('Категории')

	def __str__(self):
		return self.name

class ShopItem(models.Model):
	name = models.CharField(max_length=100,verbose_name="Наименование")
	description = models.TextField(verbose_name="Описание")
	img = models.FileField(upload_to=upload_img,blank=True, null=True,verbose_name="Изображение")
	published = models.DateTimeField(verbose_name="Дата добавления",default=timezone.now)

	class Meta:
		verbose_name = ('Товар')
		verbose_name_plural = ('Товары')
		ordering = ['-published']

	def __str__(self):
		return self.name