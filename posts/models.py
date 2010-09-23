#coding: utf-8
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
class Post(models.Model):
	class Meta:
		verbose_name = 'Запись'
		verbose_name_plural = 'Записи'
	author = models.ForeignKey(User, verbose_name='Автор', related_name='Записи')
	title = models.CharField("Заголовок", max_length=200)
	body = models.TextField("Текст")
	pub_date = models.DateTimeField("Дата создания", auto_now_add=True)
	up_date = models.DateTimeField("Последнее изменение", auto_now=True)
	def __unicode__(self):
		return self.title



