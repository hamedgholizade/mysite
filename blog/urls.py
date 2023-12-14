from django.urls import path
from blog.views import blog_view,single_view

app_name = 'blog'

urlpatterns = [
    path("",blog_view, name = "index"),
    path("single",single_view, name = "single"),

]
