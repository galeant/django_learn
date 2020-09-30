from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=250,unique=True,verbose_name='Name')
    direction = models.CharField(max_length=120,verbose_name='Direction')
    phone = models.CharField(max_length=125,verbose_name='Phone')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "restaurant"

class Recipe(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name = models.CharField(max_length=120,verbose_name='Name')
    type = models.CharField(max_length=150,
                            choices=[('BREAKFAST','breakfast'),('LUNCH','lunch'),('DINNER','dinner')]
                            )
    thumbnail = models.ImageField(upload_to='recipe_thumbnails',default="recipe_thumbnails/default.png")
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "recipe"

class Ingredient(models.Model):
    recipe = models.ManyToManyField(Recipe)
    name = models.CharField(max_length=120,verbose_name='Name')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "ingredient"