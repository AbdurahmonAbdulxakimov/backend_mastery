from django.db import models

from utils.models import BaseModel


class Poll(BaseModel):
    title = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
