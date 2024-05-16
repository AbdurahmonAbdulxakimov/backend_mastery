from django.conf import settings
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter


from books import urls as books_urls

from users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"

urlpatterns = [
    re_path(r"^search/", include(books_urls)),
    path("", include("learn_caching.urls")),
    path("teams/", include("l_celery.urls")),
    path("estate/", include("estate.urls")),
]

urlpatterns += router.urls
