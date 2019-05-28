from goods.models import Goods
# from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from django.views import View
import json
class GoodsListView(View):
    def get(self, request):
        GoodsAll = Goods.objects.all()[0:10]
        GoodJson = []
        # for good in GoodsAll:
        #     GoodList = dict()
        #     GoodList["name"] = good.name
        #     GoodList["market_price"] = good.market_price
        #     GoodList["goods_num"] = good.goods_num
        #     GoodJson.append(GoodList)

        from django.core import serializers
        json_data = serializers.serialize('json',GoodsAll)
        json_data = json.loads(json_data)
        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(json_data, content_type="application/json", safe=False)


