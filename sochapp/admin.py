from django.contrib import admin
from sochapp.models import (
    FeedbacksAndSuggestions,
    Message,
    Members,
    NewsLetter,
    Gallery,
    AnnouncementAndNews,
    AcademicResources,
    Syllabus,
    Update,
    ContactInfo,
    MemberPosition
)

admin.site.site_header = "SSOChE"


class AdminAnnouncementAndNewsAdmin(admin.ModelAdmin):
    search_fields = [
        "title",
    ]


# Register your models here.
admin.site.register(AnnouncementAndNews, AdminAnnouncementAndNewsAdmin)
admin.site.register(ContactInfo)
admin.site.register(FeedbacksAndSuggestions)
admin.site.register(Gallery)
admin.site.register(MemberPosition)
admin.site.register(Members)
admin.site.register(Message)
admin.site.register(NewsLetter)
# admin.site.register(AcademicResources)
admin.site.register(Syllabus)
admin.site.register(Update)
