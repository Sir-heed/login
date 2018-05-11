from django.contrib import admin

from .models import Post, Collection

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 
				   'published_date')
	list_filter = ('published_date', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)} #you can do this in models tho.
	#raw_id_fields = ['author']
	date_hierarchy = 'published_date'
	ordering = ['published_date']


admin.site.register(Post, PostAdmin)
admin.site.register(Collection)