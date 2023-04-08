from .models import Manual_chapter, Manual_sub_chapter, Manual_sub_chapter_content
from rest_framework import serializers

class Manual_chapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual_chapter
        fields = '__all__'
        
class Manual_sub_chapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual_sub_chapter
        fields = '__all__'
        
class Manual_sub_chapter_contentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual_sub_chapter_content
        fields = '__all__'