from django.urls import path
from . import views

urlpatterns = [
    #regular route
    path('books',views.books),
    #class route with @api_view decorator
    path('orders', views.Orders.listOrders),
    #routing class based views
    # path('books/<int:pk>',views.BookView.as_view())
    #routing class based using ViewSets
    path('booksfetch', views.BookView.as_view(
        	{
    	    'get': 'list',
    	    'post': 'create',
	        })
	),
    path('books/<int:pk>',views.BookView.as_view(
            {
            'get': 'retrieve',      
        	'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',   
            })
	)
]
