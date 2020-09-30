from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Restaurant, Recipe, Ingredient
from django.http import HttpResponse,Http404
from rest_framework import status
import requests 
from pprint import pprint


class Restaurants(APIView):

    def get(self, request):
        # restaurants = Restaurant.objects.all()
        # serializer = serializers.RestaurantSerializer(restaurants, many=True)
        # return Response(serializer.data)
        response = requests.get('https://pokeapi.co/api/v2/ability/')
        response = response.json()
        # pprint(geodata)
        # return Response(geodata)
        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964,
            "data": response
        }
        return Response(thisdict)
        # return HttpResponse(geodata)

    # def post(self, request):
    #     serializer = serializers.RestaurantSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetail(APIView):

    def get(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404
        serializer = serializers.RestaurantSerializer(restaurant)
        return Response(serializer.data)

    # def delete(self, request, restaurant_id):
    #     try:
    #         restaurant = Restaurant.objects.get(pk=restaurant_id)
    #     except Restaurant.DoesNotExist:
    #         raise Http404
    #     restaurant.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)