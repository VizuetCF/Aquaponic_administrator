from django.urls import path, include

from rest_framework import routers

from .viewsets import Manual_chapterViewSet, Manual_sub_chapterViewSet, Manual_sub_chapter_contentViewSet

router = routers.SimpleRouter()
router.register('chapter', Manual_chapterViewSet)
router.register('sub-chapter', Manual_sub_chapterViewSet)
router.register('content', Manual_sub_chapter_contentViewSet)

urlpatterns = router.urls 