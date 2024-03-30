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

    if created:
        post = PostSerializer(instance)
        data = cache.get("posts")
        data.append(post.data)
    else:
        posts = models.Post.objects.all()
        posts = PostSerializer(posts, many=True)
        cache.set("posts", posts)
    cache.set("posts", data)
