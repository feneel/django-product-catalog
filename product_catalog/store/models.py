from django.db import models

# Create your models here.


class Category(models.Model):
    name= models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name= models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name= models.CharField(max_length=200)
    description= models.TextField()
    tags= models.ManyToManyField(Tag)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    price= models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name
