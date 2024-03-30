from rest_framework import serializers

from learn_caching import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ("id", "title")
