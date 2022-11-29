from rest_framework import serializers
from .models import CartItem

class ApiSerializer(serializers.ModelSerializer):
    # product_name = serializers.CharField(max_length=200)
    # product_price = serializers.FloatField()
    # product_quantity = serializers.IntegerField(required=False, default=1)
    excel=serializers.FileField()

    class Meta:
        model = CartItem
        fields = ('__all__')