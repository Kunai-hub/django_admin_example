from _csv import reader
from decimal import Decimal

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app_goods.entities import Items
from app_goods.models import Item
from app_goods.forms import ItemForm
from app_goods.serializers import ItemSerializer


def items_list(request):
    items = Item.objects.all()
    return render(request,
                  'goods/items_list.html',
                  {'items_list': items})


def update_price(request):

    if request.method == 'POST':
        upload_file_form = ItemForm(request.POST, request.FILES)

        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['price'].read()
            price_str = price_file.decode('utf-8').split('\n')
            csv_reader = reader(price_str, delimiter=',', quotechar='"')

            for row in csv_reader:
                Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
            return HttpResponse('Цены были успешно обновлены', status=200)
    else:
        upload_file_form = ItemForm()

    return render(request,
                  'goods/upload_price_items.html',
                  {'form': upload_file_form})


def items_list_api(request):

    if request.method == 'GET':
        items_for_sale = [
            Items(
                name='Кофемашина',
                description='Отличный кофе',
                weight=1000
            ),
            Items(
                name='AirPods',
                description='Отличный звук',
                weight=1500
            )
        ]

        return JsonResponse(ItemSerializer(items_for_sale, many=True).data, safe=False)


class ItemList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)
