from rest_framework import serializers
from ..models import Post
from users.api.serializers import UserPublicSerializer

POST_VALIDATE = ['like', 'unlike']

class PostActionSerializer(serializers.Serializer):
    id = serializers.CharField()
    action = serializers.CharField()
    def validate_action(self, value):
        value = value.lower().strip()
        if value not in POST_VALIDATE:
            raise serializers.ValidationError("This is not a valid action")
        return value    
        
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