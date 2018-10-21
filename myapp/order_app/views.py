# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from order_app.models import Product
from rest_framework import filters
from order_app.serializers import ProductSerializers
from django_filters.rest_framework import DjangoFilterBackend


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filter_fields = ['store_key']




