from rest_framework import status, generics
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from .models import Menu, Booking
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes





class MenuView(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    ordering_fields = ['price']
    searching_fields = ['title']


    
class SingleMenuView(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

   
class BookingView(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    ordering_fields = ['name', 'no_of_guests', 'booking_date']
    searching_fields = ['name']

   
class SingleBookingView(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


   
class SingleBookingView(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 
    
    
# class UserView(generics.ListAPIView, generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     ordering_fields = ['username', 'email', 'groups']
#     searching_fields = ['username', 'groups']

        
   
# class SingleUserView(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


