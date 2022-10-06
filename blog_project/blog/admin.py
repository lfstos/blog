from django.contrib import admin

from .models import Blog, Author

admin.site.register(
    [Author]
)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'slug',
        'body',
        'publish',
        'status',
    ]
