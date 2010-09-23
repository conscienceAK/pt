from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
	list_display = ('username',)
	search_fields = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
#admin.site.register(CustomUser, UserAdmin)
