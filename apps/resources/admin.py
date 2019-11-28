from martor.widgets import AdminMartorWidget

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db import models

from .models import Document, Section, Subtitle


# Register your models here.

class SectionInline(admin.StackedInline):
    model = Section


@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    list_display = ['title']
    inlines = [SectionInline]
    pass


@admin.register(Section)
class SectionAdmin(ModelAdmin):
    list_display = ['title', 'md', 'get_document_title']
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

    def get_document_title(self, section: Section):
        return section.document.title

    get_document_title.short_description = 'Author'
    get_document_title.admin_order_field = 'book__author'

    pass


@admin.register(Subtitle)
class SubtitleAdmin(ModelAdmin):
    list_display = ['subtitle']

    pass
