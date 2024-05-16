import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import BookDocument


class BookDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    class Meta:
        document = BookDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            "id",
            "title",
            "published_date",
        )
