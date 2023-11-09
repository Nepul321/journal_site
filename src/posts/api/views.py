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



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_like_unlike_view(request):
    context = {"request" : request}
    serializer = PostActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        id = data.get("id")
        action = data.get("action")
        qs = Post.objects.filter(id=id)
        if not qs.exists():
            return Response({}, status=404)

        obj = qs.first()
        if action == "like":
            obj.likes.add(request.user)
            serializer = PostSerializer(obj, context=context)
            return Response(serializer.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            serializer = PostSerializer(obj, context=context)
            return Response(serializer.data, status=200)

    return Response({}, status=401)