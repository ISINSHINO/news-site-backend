from rest_framework import serializers
from news_app.models import Post
from news_app.models import Tag
from .tag_serializer import TagSerializer
from .read_write_serializer import ReadWriteSerializerMethodField


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    user = ReadWriteSerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        post = Post.objects.create(**validated_data)

        for tag_data in tags_data:
            post.tags.add(Tag.objects.get_or_create(**tag_data)[0])

        return post

    def get_user(self, obj):
        return {
            "username": obj.user.username,
            "id": obj.user.id
        }

    def to_internal_value(self, data):
        new_data = data.copy()
        tags = new_data['tags'].split(',')

        for tag in tags:
            new_data[f'tags[{tags.index(tag)}]title'] = tag

        return super().to_internal_value(new_data)
