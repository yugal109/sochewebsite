from django.urls import path
from sochapp.views import home,gallery,year,newsletter,announcement,team


urlpatterns = [
    path("",home,name="home"),
    path("gallery/",gallery,name="gallery"),
    path("year/<str:year>",year,name="year"),
    path("newsletter/",newsletter,name="newsletter"),
    path("announcement/",announcement,name="announcement"),
    path("team/",team,name="team"),
    # year(request,First)
] 
