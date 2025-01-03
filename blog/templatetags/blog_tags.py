from django import template
from blog.models import Post,Category,Comment
register = template.Library()

@register.simple_tag()
def hello():
    return "HELLO !!!"

@register.simple_tag(name="plustwo")
def function(x=5):
    return x+2

@register.simple_tag(name="totalposts")
def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name="posts")
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter()
def snippet(value,args=20):
    return value[:args] + "..."

@register.simple_tag(name="comments_count")
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()


@register.inclusion_tag("blog/blog-latest-posts.html")
def latest_posts(args=3):
    posts=Post.objects.filter(status=1).order_by('published_date')[:args]
    return {'posts': posts}

@register.inclusion_tag("blog/blog-posts-categories.html")
def posts_categories ():
    categories = Category.objects.all()
    posts = Post.objects.filter(status=1)
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('blog/next-previous-links.html')
def next_previous_links(post):
    next_post = Post.objects.filter(published_date__gt=post.published_date).order_by('published_date').first()
    prev_post = Post.objects.filter(published_date__lt=post.published_date).order_by('-published_date').first()
    return {'next_post':next_post,'prev_post':prev_post,'post':post}