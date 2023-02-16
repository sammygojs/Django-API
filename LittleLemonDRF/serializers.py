from .models import MenuItem, Category
from rest_framework import serializers
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    # category = serializers.StringRelatedField()
    # category = CategorySerializer()
    class Meta:
        model = MenuItem
        # fields = ['id','title','price','inventory']
        fields = ['id','title','price','stock','price_after_tax','category']
        # extra_kwargs = {'price':{'min_value':2},'inventory':{'min_value':0}}
        depth=1
    def calculate_tax(self, product:MenuItem):
        return product.price*Decimal(1.1)

