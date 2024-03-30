from django.urls import path

from learn_caching import views


urlpatterns = [
    path("post/", views.PostListAPIView.as_view(), name="post_list"),
]
