from django.urls import path

from estate import views


urlpatterns = [
    path("", views.EstateListAPIView.as_view()),
]
