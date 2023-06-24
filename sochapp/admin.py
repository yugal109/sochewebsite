from django.contrib import admin
from sochapp.models import FeedbacksAndSuggestions,Message,Members,NewsLetter,Gallery,AnnouncementAndNews,AcademicResources,Syllabus,Update,ContactInfo



# Register your models here.
admin.site.register(FeedbacksAndSuggestions)
admin.site.register(Message)
admin.site.register(Members)
admin.site.register(Gallery)
admin.site.register(AcademicResources)
admin.site.register(Syllabus)
admin.site.register(Update)
admin.site.register(ContactInfo)
admin.site.register(AnnouncementAndNews)
admin.site.register(NewsLetter)
