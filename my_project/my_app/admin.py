from django.contrib import admin
from . import models
# Register your models here.


class CustStudent(admin.ModelAdmin):
    list_display = ('first_name', 'student_address')
    list_display_links = ('student_address',)
    list_editable = ('first_name',)
    search_fields = ('first_name', )
    ordering = ['first_name']
    list_filter = ('age',)
    # exclude = ('std',)
    radio_fields = {'college': admin.VERTICAL}


admin.site.register(models.College)
admin.site.register(models.Student, CustStudent)
