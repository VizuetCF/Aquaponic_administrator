'''
Para realizar un CRUD en nuestro proyecto
'''

from rest_framework import viewsets

from .models import Manual_chapter, Manual_sub_chapter, Manual_sub_chapter_content
from .serializer import Manual_chapterSerializer, Manual_sub_chapterSerializer, Manual_sub_chapter_contentSerializer

class Manual_chapterViewSet(viewsets.ModelViewSet):
    queryset = Manual_chapter.objects.all()    
    serializer_class = Manual_chapterSerializer
    
class Manual_sub_chapterViewSet(viewsets.ModelViewSet):
    queryset = Manual_sub_chapter.objects.all()    
    serializer_class = Manual_sub_chapterSerializer
    
class Manual_sub_chapter_contentViewSet(viewsets.ModelViewSet):
    queryset = Manual_sub_chapter_content.objects.all()    
    serializer_class = Manual_sub_chapter_contentSerializer