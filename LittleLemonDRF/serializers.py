from .models import MenuItem, Category
from rest_framework import serializers
from decimal import Decimal

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    class Meta:
        model = MenuItem
        # fields = ['id','title','price','inventory']
        fields = ['id','title','price','stock','price_after_tax']
        # extra_kwargs = {'price':{'min_value':2},'inventory':{'min_value':0}}
    def calculate_tax(self, product:MenuItem):
        return product.price*Decimal(1.1)
    
    
# class CategorySerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id','title']

# class MenuItemSerializer(serializers.ModelSerializer):
#     # category_id = serializers.IntegerField(write_only=True)
#     category = CategorySerializer(read_only=True)
#     class Meta:
#         model = MenuItem
#         fields = ['id','title','price','inventory','category']
#         # fields = ['id','title','price','inventory','category','category_id']
    
    