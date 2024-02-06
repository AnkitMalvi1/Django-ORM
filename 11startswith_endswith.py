# __startswith, __istartswith, __endswith, __iendswith

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response 

@action(detail=False, methods=["GET"])
def lookup_filter_3(self,request,*args,**kwargs):
    title = request.GET.get('title')
    queryset = Post.objects.filter(title__startswith=title) # case-sensitive
    queryset = Post.objects.filter(title__istartswith=title) # in-case-sensitive

    queryset = Post.objects.filter(title__endswith=title) # case-sensitive
    queryset = Post.objects.filter(title__iendswith=title) # in-case-sensitive

    serializer = self.serializer_class(queryset,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)