from rest_framework import serializers
from .models import product

class productserializer(serializers.ModelSerializer):
    class meta:
        model =product
        fields=['id', 'title', 'description', 'price', 'inventory_quantity']