from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls")),
    path("feedback/", include("feedback.urls")),
    path("lessons/", include("lessons.urls")),
    path("teachers/", include("teachers.urls")),
    path("mock/", include("mockexam.urls")),

    path("payment/", include("payment.urls")),
    path("payments/", include("payme.urls")),
    path('pyclick/', include('pyclick.urls')),
    
    path("mock-payment/", include("mock_payment.urls")),
    path("lesson-types/", include("lessonType.urls")),
    path("clients/", include("clients.urls")),
    path("successful/", include("successfulStudents.urls")),
    path("form-users/", include("formUsers.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
