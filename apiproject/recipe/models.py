from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=30)
    cuisine= models.CharField(max_length=50)
    meal_type= models.CharField(max_length=50)
    ingredients= models.CharField(max_length=150)


    def __str__(self):
        return self.name

class Review(models.Model):
    recipe = models.ForeignKey(Recipe,  on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)
    comment = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe.name







