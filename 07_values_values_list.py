# .values()

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

@action(detail=False, methods=["GET"])
def get_values(self, request, pk, *args, **kwargs):
    queryset = Post.objects.filter(pk=pk).values("id","title","slug")

    serializer = PostValuesSerializer(queryset,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# .values_list()

@action(detail=False, methods=["GET"])
def get_values_list(self, request, pk, *args, **kwargs):
    queryset = Post.objects.filter(pk=pk).values_list("id","title","slug")
    return Response(queryset, status=status.HTTP_200_OK)