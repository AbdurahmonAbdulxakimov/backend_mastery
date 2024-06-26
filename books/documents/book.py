from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl_drf.compat import StringField
from elasticsearch_dsl import analyzer

from books.models import Book


# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(number_of_shards=1, number_of_replicas=1)

# html_strip = analyzer(
#     "html_strip",
#     tokenizer="standard",
#     filter=["standard", "lowercase", "stop", "snowball"],
#     char_filter=["html_strip"],
# )


@INDEX.doc_type
class BookDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr="id")

    title = StringField(
        # analyzer=html_strip,
        fields={
            "raw": StringField(analyzer="keyword"),
        },
    )

    # authors = StringField(
    #     attr="authors_indexing",
    #     # analyzer=html_strip,
    #     fields={
    #         "raw": StringField(analyzer="keyword", multi=True),
    #         "suggest": fields.CompletionField(multi=True),
    #     },
    #     multi=True,
    # )

    published_date = fields.DateField()

    class Django(object):
        """Inner nested class Django."""

        model = Book  # The model associate with this Document
