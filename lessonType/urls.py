from django.urls import path
from .views import LessonTypeApiListView

urlpatterns = [
    path("list/", LessonTypeApiListView.as_view(), name="lesson-types-list")
]
