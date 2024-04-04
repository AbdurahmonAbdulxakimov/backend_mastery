from django.db import models


class Team(models.Model):
    title = models.CharField(max_length=255)
    games_count = models.PositiveIntegerField(default=0)
    score_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title
