# __contains and __icontains

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

@action(detail=False, methods=["GET"])
def lookup_filter_2(self,request,*args,**kwargs):
    title = request.GET.get('title')
    queryset = Post.objects.filter(title__contains=title) # case-sensitive
    queryset = Post.objects.filter(title__icontains=title) # in-case-sensitive

    serializer = self.serializer_class(queryset,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)