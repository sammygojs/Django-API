from django.urls import path
from . import views

urlpatterns = [
    path('menuitems/', views.menu_items),
    # path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]