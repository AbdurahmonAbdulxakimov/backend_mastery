from django.urls import path
from l_celery.views import TeamListAPIView


urlpatterns = [path("", TeamListAPIView.as_view())]
