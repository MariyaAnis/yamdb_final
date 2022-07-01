from django.contrib import admin

from .models import Comment, Review, User, Title

admin.site.register(User)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Title)
