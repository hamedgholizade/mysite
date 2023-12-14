from django.urls import path
from website.views import about_view,index_view,contact_view,elements_view

app_name = 'website'

urlpatterns = [
    path("elements",elements_view, name = "elements"),
    path("contact-us",contact_view, name = "contact"),
    path("about-us",about_view, name = "about"),
    path("",index_view, name = "index"),
]
