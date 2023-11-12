from rest_framework.decorators import (
    api_view,
    permission_classes
)
from ..models import Post
from .serializers import (
    PostSerializer,
    PostActionSerializer
)
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.response import Response

@api_view(['GET'])
def posts_view(request, *args, **kwargs):
    context = {"request" : request}
    qs = Post.objects.all()
    serializer = PostSerializer(qs, many=True, context=context)
    data = serializer.data
    return Response(data, 200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_like_unlike_view(request, *args, **kwargs):
    user = request.user
    context = {"request" : request}
    serializer = PostActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        id = data.get("id")
        qs = Post.objects.filter(id=id)
        if not qs.exists():
            return Response({}, status=404)

        obj = qs.first()
        if not user in obj.likes.all():
            obj.likes.add(request.user)
            serializer = PostSerializer(obj, context=context)
            return Response(serializer.data, status=200)
        else:
            obj.likes.remove(request.user)
            serializer = PostSerializer(obj, context=context)
            return Response(serializer.data, status=200)

    return Response({}, status=401)