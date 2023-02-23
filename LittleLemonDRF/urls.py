from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('menu-items', views.menu_items),
    path('menu-item/<int:id>', views.single_item),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('manager-view', views.manager_view)
    # path('menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),
    # path('menu-items/<int:pk>',views.MenuItemViewSet.as_view({'get':'retrieve'})),
]

# urlpatterns = [
#     path('categories', views.CategoriesView.as_view()),
#     path('menu-items', views.MenuItemsView.as_view()),
# ]