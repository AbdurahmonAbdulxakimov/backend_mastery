from rest_framework import serializers

from estate.models import Estate


class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = ("id", "title", "price", "location", "area")
