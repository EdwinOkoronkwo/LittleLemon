from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer
from .models import MenuItem, Booking
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
class MenuItemsView(generics.ListAPIView, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price']
    searching_fields = ['title']
 
  
class SingleMenuItemView(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

   
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
    
    
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = ([IsAuthenticated])

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_superuser:
#             return User.objects.all()
#         return User.objects.filter(username=user.username)

#     def get_object(self):
#         obj = get_object_or_404(User.objects.filter(id=self.kwargs["pk"]))
#         self.check_object_permissions(self.request, obj)
#         return obj
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = ([IsAuthenticated])

        return super(UserViewSet, self).get_permissions()
