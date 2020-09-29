from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
   
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=25)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=21,decimal_places=2)
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
        null=True
    ) 

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'

class Type(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'type'

class Tag(models.Model):
    name = models.CharField(max_length=255)
    product = models.ManyToManyField(Product,through='ProductTag')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tag'

class ProductTag(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    activatio_limit = models.DateTimeField()

    class Meta:
        db_table = 'product_tag'