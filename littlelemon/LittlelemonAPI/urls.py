from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
    path('users/', views.UserViewSet.as_view({'get': 'list','post': 'create'}), name="user_view"),
    path('users/<int:pk>', views.UserViewSet.as_view({
                    'get': 'retrieve',
                     'put': 'update',
                    'patch': 'partial_update',
                    'delete': 'destroy'
                }), name="user_view_detail"),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    

]