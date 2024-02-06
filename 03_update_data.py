# .update()

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["POST"])
    def update_data(self,request,pk,*args,**kwargs):
        summary_data = request.data.get("summary")
        content_data = request.data.get("content")

        Post.objects.filter(pk=pk).update(summary=summary_data, content=content_data)

        return Response({"message": "Successfully updated the data."})


# .update_or_create()

    @action(detail=False, methods=["POST"])
    def update_or_create_data(self,request,*args,**kwargs):
        category_data = set(request.data.get("category"))
        summary_data = request.data.get("summary")
        content_data = request.data.get("content")
        title_data = request.data.get("title")
        author = 1

        obj, _ = Post.objects.update_or_create(
            title=title_data,
            defaults={
                "summary":summary_data,
                "content":content_data,
                "author_id":author
            }
        )
        obj.category.set(category_data)

        return Response({"message": "Successfully updated the data."})


# .bulk_update()

    @action(detail=False, methods=["POST"])
    def bulk_update_data(self,request,*args,**kwargs):
        ids = request.data.get("ids")
        queryset = Post.objects.filter(id__in=ids)

        for obj in queryset:
            obj.status = STATUS.PUBLISH.value

        Post.objects.bulk_update(queryset,["status"])    

        return Response({"message": "Successfully updated the data."})