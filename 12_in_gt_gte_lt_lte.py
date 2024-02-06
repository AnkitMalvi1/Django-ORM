# __in, __gt, __gte, __lt, __lte

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response 

@action(detail=False, methods=["GET"])
def lookup_filter_4(self,request,*args,**kwargs):
    ids = request.GET.get('ids')
    ids = ids.split(",")
    queryset = Post.objects.filter(id__in=ids) 
    queryset = Post.objects.filter(ids__gt=ids) 
    queryset = Post.objects.filter(ids__gte=ids) 
    queryset = Post.objects.filter(ids__lt=ids) 
    queryset = Post.objects.filter(ids__lte=ids)

    serializer = self.serializer_class(queryset,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@action(detail=False, methods=["GET"])
def lookup_filter_5(self,request,*args,**kwargs):
    views = request.GET.get("views")
    queryset = Post.objects.filter(views__gt=views) 
    queryset = Post.objects.filter(views__gte=views) 
    queryset = Post.objects.filter(views__lt=views) 
    queryset = Post.objects.filter(views__lte=views)

    serializer = self.serializer_class(queryset,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)