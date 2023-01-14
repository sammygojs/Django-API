from .models import MenuItem
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    return Response(items.values())