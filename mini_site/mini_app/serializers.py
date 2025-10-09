from .models import Category, Product
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class ProductSerializer(serializers.ModelSerializer):
    created_data = serializers.DateTimeField(format='%d-$m-%Y %H:$M')

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'phone_number',
                  'description', 'product_type', 'created_data', 'image']