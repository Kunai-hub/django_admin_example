from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_blank=True)
    weight = serializers.FloatField(min_value=0)
