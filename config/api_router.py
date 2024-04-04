from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"

urlpatterns = [
    path("", include("learn_caching.urls")),
    path("teams/", include("l_celery.urls")),
    path("estate/", include("estate.urls")),
]
urlpatterns += router.urls
