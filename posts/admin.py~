from django.contrib import admin
from models import Post
class PostAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		if not change:
			obj.author = request.user
		obj.save()	
	fields = ('title', 'body')
	list_display = ('title', 'author', 'pub_date')
	date_hierarchy = 'pub_date'

admin.site.register(Post, PostAdmin)
