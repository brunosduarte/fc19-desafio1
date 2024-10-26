from django.contrib import admin

from core.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...