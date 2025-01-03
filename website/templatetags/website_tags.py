from django import template
from blog.models import Post,Category
register = template.Library()

@register.inclusion_tag("website/recent-blog-posts.html")
def recent_blog_posts(args=6):
    posts=Post.objects.filter(status=1).order_by('published_date')[:args]
    return {'posts': posts}