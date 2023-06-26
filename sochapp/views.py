from django.shortcuts import render, redirect
from sochapp.models import (
    FeedbacksAndSuggestions,
    Members,
    MemberPosition,
    Gallery,
    Syllabus,
    Message,
    AnnouncementAndNews,
)
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages

# Create your views here.


def home(request):
    msgs = Message.objects.all()
    announce_and_news = AnnouncementAndNews.objects.all().order_by("-created_at")[:3]

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        FeedbacksAndSuggestions.objects.create(
            title=subject, description=message, email=email, full_name=name
        )
        messages.add_message(
            request, messages.SUCCESS, "Successfully submitted your feedback."
        )
        return redirect("/#contact")

        # pass
    return render(
        request,
        "sochapp/home.html",
        {"msgs": msgs, "announce_and_news": announce_and_news},
    )


def gallery(request):
    gal = Gallery.objects.all()
    p = Paginator(gal, 1)

    page_number = request.GET.get("page")
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.pa
    return render(request, "sochapp/gallery.html", {"page_obj": page_obj})


def year(request, year):
    year_from_db = Syllabus.objects.filter(year=year)

    return render(
        request, "sochapp/year.html", {"year": year, "year_from_db": year_from_db}
    )


def newsletter(request):
    return render(request, "sochapp/newsletter.html")


def announcement(request):
    anns = AnnouncementAndNews.objects.all().order_by("-created_at")
    p = Paginator(anns, 3)

    page_number = request.GET.get("page")
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    return render(request, "sochapp/announcement.html", {"page_obj": page_obj})

def team(request):
    # ts=Members.objects.all().values("id")
    ts=[]
    position=MemberPosition.objects.all().order_by("order")

    for i in range(0,position.count()):
        # ts[i]=
        # Members.objects.filter(position=position[i])
        x= Members.objects.filter(position=position[i])
        ts.append(x)

    return render(request, "sochapp/teammembers.html",{"ts":ts})
