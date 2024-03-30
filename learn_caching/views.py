from django.core.cache import cache
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from learn_caching import models, serializers


class PostListAPIView(ListAPIView):
    queryset = models.Post.objects.all()[:100]
    serializer_class = serializers.PostSerializer

    def get(self, request):
        posts = cache.get("posts", None)
        if posts:
            return Response(posts)
        return super().get(request)

    def list(self, request, *args, **kwargs):
        posts = super().list(request)
        cache.set("posts", posts.data)
        return Response(posts.data)
