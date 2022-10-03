from django.contrib import admin

from news_app.models.post_model import Post
from news_app.models.tag_model import Tag
from news_app.models.user_model import User

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Tag)
