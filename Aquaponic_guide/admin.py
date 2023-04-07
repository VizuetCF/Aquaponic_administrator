from django.contrib import admin
from .models import Manual_chapter, Manual_sub_chapter, Manual_sub_chapter_content

# Register your models here.

admin.site.register(Manual_chapter)
admin.site.register(Manual_sub_chapter)
admin.site.register(Manual_sub_chapter_content)