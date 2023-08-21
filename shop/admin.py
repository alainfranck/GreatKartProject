from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . models import *

# Register your models here.
class SecusigneAdmin(SummernoteModelAdmin):
    list_display = ('titre',)
    prepopulated_fields = {"slug": ("titre",)}
    summernote_fields = ('description',)

class GuideAdmin(SummernoteModelAdmin):
    list_display = ('titre',)
    prepopulated_fields = {"slug": ("titre",)}
    summernote_fields = ('description',)


admin.site.register(Secusigne, SecusigneAdmin)
admin.site.register(Guide, GuideAdmin)
