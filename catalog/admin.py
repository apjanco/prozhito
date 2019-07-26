from django.contrib import admin

# Register your models here.
from catalog.models import *
from django.utils.html import format_html


"""
admin.site.register(Publication)
admin.site.register(Author)
admin.site.register(Edition)
"""
# Define the admin class

# Register the admin class using the decorator

"""
class DiaryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Diary, DiaryAdmin)
"""