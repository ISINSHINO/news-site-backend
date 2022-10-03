from rest_framework import viewsets

from news_app.models import Post
from news_app.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer