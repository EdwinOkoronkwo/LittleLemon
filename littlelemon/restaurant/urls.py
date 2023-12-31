from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuView.as_view(), name="menu_list_view"),
    path('menu/<int:pk>', views.SingleMenuView.as_view(), name="menu_single_view"),
    path('booking', views.BookingView.as_view(), name="booking_list_view"),
    path('booking/<int:pk>', views.SingleBookingView.as_view(), name="booking_single_view"),
    path('api-token-auth/', obtain_auth_token),
    # path('users', views.UserView.as_view(), name="user_list_view"),
    # path('users/<int:pk>', views.SingleUserView.as_view(), name="user_single_view"),
 
]
