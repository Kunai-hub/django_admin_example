from rest_framework import serializers

from app_goods.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'weight']
