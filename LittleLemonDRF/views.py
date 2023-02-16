from django.shortcuts import render,get_object_or_404
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
# , CategorySerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def menu_items(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_items = MenuItemSerializer(items, many=True)
    return Response(serialized_items.data)
    # return Response(items.values())

@api_view()
def single_item(request,id):
    item = get_object_or_404(MenuItem,pk=id)
    serialized_items = MenuItemSerializer(item)
    return Response(serialized_items.data)

# Create your views here.
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

# Create your views here.
# from .serializers import MenuItemSerializer, CategorySerializer

# class CategoriesView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
#     ordering_fields = ['price', 'inventory']
#     filterset_fields = ['price', 'inventory']
#     search_fields = ['title']