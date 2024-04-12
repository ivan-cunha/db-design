from django.contrib import admin

from .models import Article, ArticleComment, Comment, Link, Person

# Register the models with the admin interface
admin.site.register(Person)
admin.site.register(Article)
admin.site.register(ArticleComment)
admin.site.register(Comment)
admin.site.register(Link)
