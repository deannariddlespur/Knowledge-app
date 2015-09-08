from django.contrib import admin

from .models import Content, Question


class QuestionAdmin(admin.TabularInline):
    model = Question


class ContentAdmin(admin.ModelAdmin):
    inlines = [
        QuestionAdmin,
    ]


admin.site.register(Content, ContentAdmin)
