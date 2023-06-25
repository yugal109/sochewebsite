from django.urls import path
from sochapp.views import home,gallery,year,newsletter,announcement


urlpatterns = [
    path("",home,name="home"),
    path("gallery/",gallery,name="gallery"),
    path("year/<str:year>",year,name="year"),
    path("newsletter/",newsletter,name="newsletter"),
    path("announcement/",announcement,name="announcement"),
    # year(request,First)
] 
