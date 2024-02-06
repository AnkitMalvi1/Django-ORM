# .all()

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

@action(detail=False, methods=["GET"])
def get_all(self,request,*args,**kwargs):
    queryset = Post.objects.all()
    serializer = self.serializer_class(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


# .get()

@action(detail=False, methods=["GET"])
def get_one(self,request,*args,**kwargs):
    slug = request.GET.get("slug")

    try:
        obj = Post.objects.get(slug=slug)
    except Post.MultipleObjectsReturned:
        return Response(
            {"message": "Multiple objects found."},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Post.DoesNotExist:
        return Response(
            {"message": "Multiple not found."},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = self.serializer_class(obj)
    return Response(serializer.data, status=status.HTTP_200_OK)    


# .filter()
@action(detail=False, methods=["GET"])
def get_filter(self,request,*args,**kwargs):
    id = request.GET.get("id")
    queryset = Post.objects.filter(id=id)
    
    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)  


# .filter().first()
@action(detail=False, methods=["GET"])
def get_filter(self,request,*args,**kwargs):
    id = request.GET.get("id")
    obj = Post.objects.filter(id=id).first()
    
    serializer = self.serializer_class(obj)
    return Response(serializer.data, status=status.HTTP_200_OK)  