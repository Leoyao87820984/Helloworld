from django.contrib import admin
from .models import Post,Comment


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "published_date", "created_date"]
	list_display_links = ["published_date"]
	list_filter = ["published_date", "created_date"]
	search_fields = ["title"]
	class Meta:
		model = Post

admin.site.register(Post,PostModelAdmin)
# Register your models here.
admin.site.register(Comment)