from django.core.cache import cache
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from learn_caching import models, serializers


class PostListAPIView(ListAPIView):
    queryset = models.Post.objects.all().order_by("id")
    serializer_class = serializers.PostSerializer

    def list(self, request, *args, **kwargs):
        posts = cache.get("posts", None)
        if posts is None:
            queryset = self.filter_queryset(self.get_queryset())
            posts = self.get_serializer(queryset, many=True)
            cache.set("posts", posts.data, 60 * 15)
            return Response(posts.data)
        return Response(posts)
