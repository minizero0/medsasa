from django.contrib import admin
from .models import Theme, Comment, Hashtag

# Register your models here.
admin.site.register(Theme)
admin.site.register(Comment)
admin.site.register(Hashtag)
