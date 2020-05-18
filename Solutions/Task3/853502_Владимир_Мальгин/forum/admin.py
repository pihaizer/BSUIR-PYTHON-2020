from django.contrib import admin

from .models import *


class ThemeInline(admin.StackedInline):
    model = Theme


class MessageInline(admin.TabularInline):
    model = Message


class TopicAdmin(admin.ModelAdmin):
    inlines = [
        ThemeInline
    ]


class ThemeAdmin(admin.ModelAdmin):
    inlines = [
        MessageInline
    ]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Message)
