#coding: utf-8
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, UserManager


class CustomUser(User):
    	surname = models.CharField("Фамилия", max_length=200,)
	name = models.CharField("Имя", max_length=200,)
	city = models.CharField("Город", max_length=200,)
	job = models.CharField("Деятельность", max_length=200,) 
	interests = models.CharField("Интересы", max_length=200,)
	about = models.CharField("О себе)", max_length=200,)
	achievements = models.CharField("Достижения", max_length=200,)
	deserts = models.CharField("Заслуги", max_length=200,)
   	
	objects = UserManager()
	

