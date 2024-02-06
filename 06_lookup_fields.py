# .order_by()

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

@action(detail=False, methods=["GET"])
def order_by_data(self,request,*args,**kwargs):
    queryset = Post.objects.all().order_by("title")
    # queryset = Post.objects.all().order_by("-title")
    # queryset = Post.objects.all().order_by("-title","slug")
    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# .distinct()

@action(detail=False, methods=["GET"])
def distinct_data(self,request,*args,**kwargs):
    queryset = (
        Post.objects.all().filter(category__id__in=[1,2]).distinct()
    )

    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# deep filter // Nested lookup filter

@action(detail=False, methods=["GET"])
def deep_filter_data(self,request,*args,**kwargs):
    queryset = Post.objects.all().filter(category__id__in=[2,3]).distinct()

    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

