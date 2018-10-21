from order_app.models import Product
from rest_framework import serializers


class ProductSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('store_key', 'product_name')
