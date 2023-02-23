from django.shortcuts import render,get_object_or_404
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, throttle_classes

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import TenCallsPerMinute

@api_view(['GET','POST'])
def menu_items(request):
    # return Response('list of books',status.HTTP_200_OK)
    if request.method=='GET':
        items = MenuItem.objects.select_related('category').all()
        to_price = request.query_params.get('to_price')
        category_name = request.query_params.get('category')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage',default=3)
        page = request.query_params.get('page',default=1)
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(title__contains=search)
        if ordering:
            ordering_fields = ordering.split(',')
            items = items.order_by(*ordering_fields)

        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
        serialized_items = MenuItemSerializer(items, many=True)
        return Response(serialized_items.data)
        # return Response(items.values())
    if request.method=='POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def single_item(request,id):
    item = get_object_or_404(MenuItem,pk=id)
    serialized_items = MenuItemSerializer(item)
    return Response(serialized_items.data)

@api_view()
@permission_classes([IsAuthenticated]) #return a secret message for authenticated users only
def secret(request):
    return Response({"message":"Some secret message"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='manager').exists():
        return Response({"message":"only manager should see this message"})
    else:
        return Response({"message":"you are not authorized"},403)

@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"successful"})

@api_view()
@permission_classes([IsAuthenticated])
# @throttle_classes([UserRateThrottle])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response({"message":"msg for logged in user only"})

# from rest_framework import viewsets
# Create your views here.
# class MenuItemsViewSet(viewsets.ModelViewSet):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
#     ordering_fields = ['price', 'inventory']
#     filterset_fields = ['price', 'inventory']
#     search_fields = ['title']

# class MenuItemViewSet(viewsets.ModelViewSet ):
#     queryset = get_object_or_404(MenuItem,pk=id)
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