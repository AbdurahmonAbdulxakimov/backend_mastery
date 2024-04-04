from rest_framework import serializers

from l_celery.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "title", "games_count", "score_count")
