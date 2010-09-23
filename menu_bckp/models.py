#coding: utf-8
from django.db import models

class Menu(models.Model):
	class Meta:
		verbose_name = 'Главное меню'
	item = models.CharField("Раздел", max_length=50)
	def __unicode__(self):
		return self.item

class Info(models.Model):
	menu_item = models.ForeignKey(Menu, verbose_name="Раздел")
	title = models.CharField("Заголовок", max_length=200)
	body = models.TextField("Текст статьи")
	pub_date = models.DateTimeField("Дата создания", auto_now_add=True)
	up_date = models.DateTimeField("Последнее изменение", auto_now=True)
	def __unicode__(self):
		return self.title
