from django.urls import path
from . import views

urlpatterns = [
    #regular route
    path('books',views.books),
    #class route with @api_view decorator
    path('orders', views.Orders.listOrders)
    # path('books/<int:pk>',views.book),
]
