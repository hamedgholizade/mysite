from django.urls import path
from blog.views import blog_view,single_view,test_view,blog_search
from blog.feeds import LatestEntriesFeed

app_name = 'blog'

urlpatterns = [
    path('',blog_view, name = "index"),
    path('<int:pid>',single_view, name = "single"),
    path('tag/<str:tag_name>',blog_view, name = "tag"),
    path('category/<str:cat_name>',blog_view, name = "category"),
    path ('author/<str:author_name>',blog_view, name = "author"),
    path ('search/',blog_search, name = "search"),
    path("rss/feed/", LatestEntriesFeed()),
    path('test',test_view,name="test")
]
