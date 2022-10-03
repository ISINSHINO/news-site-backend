from rest_framework import viewsets

from news_app.models import Tag
from news_app.serializers import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer