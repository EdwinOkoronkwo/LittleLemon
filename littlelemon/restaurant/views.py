from django.shortcuts import render
from rest_framework import status, generics
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from .models import Menu, Booking
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes




# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuView(generics.ListAPIView, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    ordering_fields = ['price']
    searching_fields = ['title']
    


    
class SingleMenuView(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

   
class BookingView(generics.ListAPIView, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    ordering_fields = ['name', 'no_of_guests', 'booking_date']
    searching_fields = ['name']

   
class SingleBookingView(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


   
class SingleBookingView(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    


