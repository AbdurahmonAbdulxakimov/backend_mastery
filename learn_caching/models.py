from django.db import models

from utils.models import BaseModel


class Post(BaseModel):
    """
    Post model
    """

    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
