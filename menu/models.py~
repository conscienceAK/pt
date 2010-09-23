#coding: utf-8
from django.db import models

class Menu(models.Model):
	class Meta:
		verbose_name = 'Главное меню'
		verbose_name_plural = "Главные меню"
	name = models.CharField("Раздел", max_length=100)
	slug = models.SlugField()
	base_url = models.CharField(max_length=100, blank=True, null=True)
   	description = models.TextField(blank=True, null=True)

	class Admin:
		pass

	def __unicode__(self):
        	return "%s" % self.name

    	def save(self):
 
        	super(Menu, self).save()

        	current = 10
        	for item in MenuItem.objects.filter(menu=self).order_by('order'):
            		item.order = current
            		item.save()
            		current += 10

class MenuItem(models.Model):
    	menu = models.ForeignKey(Menu)
    	order = models.IntegerField()
    	link_url = models.CharField(max_length=100, help_text='URL or URI to the content, eg /about/ or http://foo.com/')
    	title = models.CharField(max_length=100)
    	login_required = models.NullBooleanField(blank=True, null=True)

	class Admin:
        	pass

    	def __unicode__(self):
        	return "%s %s. %s" % (self.menu.slug, self.order, self.title)

class Info(models.Model):
	menu_item = models.ForeignKey(MenuItem, verbose_name="Раздел")
	title = models.CharField("Заголовок", max_length=200)
	body = models.TextField("Текст статьи")
	pub_date = models.DateTimeField("Дата создания", auto_now_add=True)
	up_date = models.DateTimeField("Последнее изменение", auto_now=True)
	def __unicode__(self):
		return self.title

class News(models.Model):
	title = models.CharField("Заголовок новости", max_length=300)
	body = models.TextField("Текст новости")
	pub_date = models.DateTimeField("Дата создания", auto_now_add=True)
