from .models import MenuItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404

@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)

@api_view()
def single_item(request,id):
    item = get_object_or_404(MenuItem,pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)