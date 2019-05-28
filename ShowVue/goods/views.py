from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Goods
from rest_framework import status
# Create your views here.

class GoodsListView(APIView):
    """
    序列化商品
    """
    def get(self, request):
        goods = Goods.objects.all()[:10]
        good_serializer =GoodsSerializer(goods,many=True)
        return Response(good_serializer.data)

    def post(self, request, form=None):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



