from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.menu_items),
    path('menu-item/<int:id>', views.single_item),
    # path('menu-items', views.MenuItemsView.as_view()),
    # path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]

# urlpatterns = [
#     path('categories', views.CategoriesView.as_view()),
#     path('menu-items', views.MenuItemsView.as_view()),
# ]