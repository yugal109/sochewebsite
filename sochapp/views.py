from django.shortcuts import render,redirect
from sochapp.models import FeedbacksAndSuggestions,Gallery,Syllabus,Message,AnnouncementAndNews
from django.contrib import messages

# Create your views here.

def home(request):
    msgs=Message.objects.all()
    announce_and_news=AnnouncementAndNews.objects.all().order_by("-created_at")[:4]

    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]

        FeedbacksAndSuggestions.objects.create(title=subject,description=message,email=email,full_name=name)
        messages.add_message(request, messages.SUCCESS, 'Successfully submitted your feedback.')
        return redirect("/#contact")

        # pass
    return render(request,"sochapp/home.html",{"msgs":msgs,"announce_and_news":announce_and_news})

def gallery(request):
    gal=Gallery.objects.all()
    return render(request,"sochapp/gallery.html",{"gallery":gal})

def year(request,year):
    year_from_db=Syllabus.objects.filter(year=year)

    return render(request,"sochapp/year.html",{"year":year,"year_from_db":year_from_db})



def newsletter(request):
    return render(request,"sochapp/newsletter.html")


