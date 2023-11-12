from rest_framework import serializers
from ..models import Post
from users.api.serializers import UserPublicSerializer


class PostActionSerializer(serializers.Serializer):
    id = serializers.CharField()
        
class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    author = UserPublicSerializer(read_only=True)
    is_author = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'content', 'author', 'likes',  'is_author', 'date')

    def get_likes(self, obj):
        return obj.likes.count()
        
    def get_is_author(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
        return False