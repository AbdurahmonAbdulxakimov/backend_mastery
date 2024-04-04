from django.db import models


class Estate(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=255)
    area = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
