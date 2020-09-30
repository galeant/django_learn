from rest_framework import serializers
from . import models
import base64
from django.conf import settings
import os

class RestaurantSerializer(serializers.ModelSerializer):
    # Serializer for the Restaurant model, in fields we specify the model attributes we want to
    # deserialize and serialize
    class Meta:
        model = models.Restaurant
        fields = ['id', 'name', 'direction', 'phone']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ['id', 'name']
