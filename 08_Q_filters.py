# .values()

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

@action(detail=True, methods=["GET"])
def q_filter(self,request,pk,*args,**kwargs):
    # queryset = Post.objects.filter(Q(pk=pk))
    # queryset = Post.objects.filter(~Q(pk=pk))

    # OR filter
    queryset = Post.objects.filter(Q(pk=pk)|Q(author=pk))

    # AND filter
    queryset = Post.objects.filter(Q(pk=pk)&Q(author=pk))

    # queryset = Post.objects.filter(~Q(pk=pk)&Q(author=pk))
    # queryset = Post.objects.filter(Q(~Q(pk=pk)&Q(author=pk)) & Q(category__in=[pk]))

    serializer = self.serializer_class(queryset,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)