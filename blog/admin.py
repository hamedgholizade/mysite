from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["id", "title","author","counted_view","status","login_required","created_date"]
    list_filter = ("status","author","category")
    #ordering = ["created_date"]
    search_fields = ["title","content"]
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["name", "email","post","approved"]
    list_filter = ("post","email","approved")
    search_fields = ["name","email","subject"]

admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)