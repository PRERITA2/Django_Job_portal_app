from pyexpat import model
from django.contrib import admin

from jobapp.models import Author, JobLocation, JobPost, Skills

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display=('title','salary','date_posted')
    list_filter=['title','salary']
    search_fields=['title','description']
    search_help_text='Search based on title and description'
    fieldsets = (
        ('Basic information',{'fields':('title','description','job_location','skills')}),
        ('More information',{'classes':('collapse','wide'),
                            'fields':(('expiry','salary'),'slug')}),
    )

admin.site.register(JobPost,JobAdmin)
admin.site.register(JobLocation)
admin.site.register(Skills)
admin.site.register(Author)