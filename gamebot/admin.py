from django.contrib import admin
from gamebot.models import CommunicationCategory


@admin.register(CommunicationCategory)
class CommunicationCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["id",]
