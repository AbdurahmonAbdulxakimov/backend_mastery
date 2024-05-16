from django.db import models


class Estate(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField(default=0)
    location = models.CharField(max_length=255)
    area = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
