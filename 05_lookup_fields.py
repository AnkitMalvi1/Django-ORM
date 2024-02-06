# .exclude()

from rest_framework import viewsets, status
from rest_framework.response import Response

def exclude_filter(self,request,*args,**kwargs):
    id = request.GET.get("id")
    queryset = Post.objects.exclude(id=id)

    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 

# limit[:2]
def exclude_filter(self,request,*args,**kwargs):
    id = request.GET.get("id")
    queryset = Post.objects.all()[:2]

    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 

# lookup filter __in
def lookup_filter(self,request,*args,**kwargs):
    ids = request.GET.get("ids")
    ids = ids.split(",")
    queryset = Post.objects.filter(id__in=ids)

    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 