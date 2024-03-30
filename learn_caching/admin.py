from django.contrib import admin

from learn_caching.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("title",)
    readonly_fields = ("created_at", "updated_at")
    ordering = ("id",)
