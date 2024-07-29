from django.shortcuts import render
from django.core.cache import cache
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from category.models import Category
from rating.serializers import RatingSerializer

from .models import Product, Appointment, Talon
from .permissions import IsAuthor
from .serializers import ProductSerializer, AppointmentSerializer, TalonSerializer
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
class ProductFilter(filters.FilterSet):
    min_price=filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    title=filters.CharFilter(field_name='title', lookup_expr='icontains')
    category=filters.ModelChoiceFilter(queryset=Category.objects.all())

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductFilter

    def perform_create(self, serializer):
        cache.delete('product_list')
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update','destroy']:
            return (IsAuthor(),)
        return (permissions.IsAuthenticatedOrReadOnly(),)
    # def list(self, request , *args, **kwargs ):
    #     cache_key='product_list'
    #     cache_response=cache.get(cache_key)
    #     if cache_response:
    #         return cache_response
    #     response=super().list(request, *args,**kwargs)
    #     cache.set(cache_key, response, 60*15)
    #     return response

    @action(['GET', 'POST' , 'DELETE'],detail=True)
    def ratings(self, request, pk):
        product=self.get_object()
        user=request.user
        if request.method=='GET':
            rating=product.ratings.all()
            serializer=RatingSerializer(instance=rating, many=True)
            return Response(serializer.data, status=200)
        elif request.method=='POST':
            if product.ratings.filter(owner=user).exists():
                return Response('Ты уже поставил рейтинг', status=400)

            # rating = product.ratings.all()
            serializer = RatingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner=user, product=product)
            return Response(serializer.data, status=201)
        else:
            if not product.ratings.filter(owner=user).exists():
                return Response('Ты не можешь кдалить ты не оставил оценку на товар', status=400)
            rating = product.ratings.get(owner=user)
            rating.delete()
            return Response('Успешно удален', status=204)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer



class TalonViewSet(viewsets.ModelViewSet):
    queryset = Talon.objects.all()
    serializer_class = TalonSerializer
# Create your views here.
