
from rest_framework import generics, filters
from .serializers import ItemSerializer
from .models import Item
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class ItemList(generics.ListAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    search_fields=['name', 'price']