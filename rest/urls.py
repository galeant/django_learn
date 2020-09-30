
from django.urls import path
from . import views

urlpatterns = [
    path('/restaurant', views.Restaurants.as_view()),
    path('restaurant/<str:restaurant_id>/', views.RestaurantDetail.as_view()),
    # path('restaurants/<str:restaurant_id>/recipes/', views.Recipes.as_view()),
    # path('restaurants/<str:restaurant_id>/recipes/<str:recipe_id>/', views.RecipeDetail.as_view()),
]