from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Comment
from .serializers import CommentSerializer
from posts.models import Post

@api_view(["GET"])
def CommentsView(request, *args, **kwargs):
    context = {"request" : request}
    qs = Comment.objects.all().order_by('-datetime')
    serializer = CommentSerializer(qs, many=True, context=context)
    data = serializer.data
    return Response(data, status=200)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def CommentCreateView(request, *args, **kwargs):
    context = {"request" : request}
    data = request.data
    content = data['content']
    post_id = data['post_id']
    if not post_id or not content:
        return Response({"detail" : "Data missing"}, status=401)
    
    if content == "":
        return Response({"detail" : "No content"}, status=401)

    obj = None

    qs = Post.objects.filter(id=int(post_id))
    if not qs:
        return Response({"detail" : "Post not found"}, status=404)
    obj = qs.first()

    comment = Comment.objects.create(
            user=request.user,
            content=content
    )

    obj.comments.add(comment)


    serializer = CommentSerializer(comment, context=context)
    return Response(serializer.data, status=201)

    
@api_view(['GET', 'DELETE', 'PUT'])
def CommentView(request, id, *args, **kwargs):
    context = {"request" : request}
    qs = Comment.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Comment not found"}, status=404)
    obj = qs.first()
    if request.method == "DELETE":
        if obj.user == request.user:
            obj.delete()
            return Response({"detail" : "Comment deleted"}, status=200)
        else:
            return Response({"detail" : "You can't delete this comment"}, status=403)
    if request.method == "PUT":
        if obj.user == request.user:
            data = request.data
            serializer = CommentSerializer(instance=obj, data=data, context=context)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
        else:
            return Response({"detail" : "You can't edit this comment"}, status=403)

    serializer = CommentSerializer(obj, context=context)
    data = serializer.data
    return Response(data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CommentReplyCreateView(request, id,  *args, **kwargs):
    context = {"request" : request}
    qs = Comment.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Comment not found"}, status=404)

    obj = qs.first()
    data = request.data
    serializer = CommentSerializer(data=data, context=context)
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            user=request.user,
            parent=obj
        )

        return Response(serializer.data, status=201)

    return Response({}, status=401)