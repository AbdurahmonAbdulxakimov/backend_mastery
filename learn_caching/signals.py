from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

from learn_caching import models
from learn_caching.serializers import PostSerializer


@receiver(post_save, sender=models.Post)
def post_save_handler(sender, instance, created, **kwargs):
    """
    Post save signal handler
    """
    posts = models.Post.objects.all().order_by("id")
    serializer = PostSerializer(posts, many=True)
    cache.set("posts", serializer.data, 60 * 15)
