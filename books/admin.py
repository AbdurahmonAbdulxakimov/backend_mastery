from django.contrib import admin

from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Book admin."""

    list_display = (
        "title",
        "published_date",
    )
    search_fields = ("title",)
    filter_horizontal = ("authors",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Author admin."""

    list_display = ("name",)
    search_fields = ("name",)
