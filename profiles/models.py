#coding: utf-8
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, UserManager


class CustomUser(User):
    	surname = models.CharField("Фамилия", max_length=200,blank=True)
	name = models.CharField("Имя", max_length=200,blank=True)
	city = models.CharField("Город", max_length=200,blank=True)
	job = models.CharField("Деятельность", max_length=200,blank=True) 
	interests = models.CharField("Интересы", max_length=200,blank=True)
	about = models.CharField("О себе)", max_length=200,blank=True)
	achievements = models.CharField("Достижения", max_length=200,blank=True)
	deserts = models.CharField("Заслуги", max_length=200,blank=True)
   	
	objects = UserManager()
	

