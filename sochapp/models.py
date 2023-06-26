from django.db import models

# Create your models here.


class FeedbacksAndSuggestions(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False)
    description = models.TextField(max_length=10000, blank=False, null=False)
    email = models.EmailField()
    full_name = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return f"{self.full_name} sent feedback - {self.title}."

    class Meta:
        verbose_name_plural = "Feedbacks"


class Message(models.Model):
    MESSAGE_CHOICES = (
        ("dean", "dean"),
        (
            "hod",
            "hod",
        ),
        ("dhod", "dhod"),
        ("president", "president"),
    )

    title = models.CharField(
        max_length=20, choices=MESSAGE_CHOICES, blank=False, null=False
    )

    message = models.TextField(blank=False, null=False, max_length=1000)
    full_name = models.CharField(max_length=200, default="", blank=False, null=False)

    image = models.ImageField(upload_to="media/images/message", blank=False, null=False)

    def __str__(self):
        return self.title


class MemberPosition(models.Model):
    position = models.CharField(max_length=20, blank=False, null=False,unique=True)
    order=models.IntegerField(default=0,blank=False,null=False)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name_plural = "MemberPosition"



class Members(models.Model):
    position = models.ForeignKey(MemberPosition,on_delete=models.CASCADE)
    message = models.TextField(blank=False, null=False, max_length=1000)
    image = models.ImageField(upload_to="media/images/members", blank=False, null=False)
    full_name = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return self.position.position

    class Meta:
        verbose_name_plural = "Members"


class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField(blank=False, null=False, max_length=1000)
    image = models.ImageField(upload_to="media/images/gallery", blank=False, null=False)

    def __str__(self):
        return self.title


class AcademicResources(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False, max_length=100000)

    file = models.FileField(upload_to="media/files/academic", blank=False, null=False)

    def __str__(self):
        return self.title


class Syllabus(models.Model):
    LEVEL_CHOICES = (
        ("First", "First"),
        ("Second", "Second"),
        ("Third", "Third"),
        ("Fourth", "Fourth"),
    )
    PART_CHOICES = (
        ("1st", "1st"),
        ("2nd", "2nd"),
    )
    year = models.CharField(
        max_length=20, choices=LEVEL_CHOICES, blank=False, null=False
    )
    part = models.CharField(
        max_length=20, choices=PART_CHOICES, blank=False, null=False
    )
    description = models.TextField(blank=False, null=False, max_length=100000)
    file = models.FileField(upload_to="media/files/syllabus", blank=False, null=False)
    resource_link = models.CharField(max_length=100000, default="")

    def __str__(self):
        return f"{self.year}/{self.part}"

    class Meta:
        verbose_name_plural = "Syllabus/Resources"


class Update(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField(blank=False, null=False, max_length=1000)
    file = models.FileField(upload_to="media/files/update", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    title_or_name = models.CharField(max_length=200, blank=False, null=False)
    contact = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.title_or_name


class AnnouncementAndNews(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField(blank=False, null=False, max_length=1000)
    image = models.FileField(
        upload_to="media/images/announcement", blank=False, null=False
    )

    file = models.FileField(
        upload_to="media/files/announcement", blank=False, null=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Announcements"


class NewsLetter(models.Model):
    image = models.ImageField(
        upload_to="media/images/newsletter", blank=False, null=False
    )

    class Meta:
        verbose_name_plural = "NewsLetter"
