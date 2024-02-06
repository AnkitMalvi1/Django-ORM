# .add()

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["PATCH"])
    def add_category(self, request, pk, *args, **kwargs):
        categories_data = request.data.get("ids")
        instance = Post.objects.filter(pk=pk).first()

        categories_data = set(categories_data)
        instance.category.add(*categories_data)

        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# .set()
    @action(detail=True, methods=["PATCH"])
    def add_category(self, request, pk, *args, **kwargs):
        categories_data = request.data.get("ids")
        instance = Post.objects.filter(pk=pk).first()

        instance.category.set(*categories_data)

        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
