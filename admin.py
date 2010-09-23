#from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import *

#class CustomUserAdmin(admin.ModelAdmin):
#	list_display = ('user', 'date')
	# search_fields = ('name',)

#admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)
