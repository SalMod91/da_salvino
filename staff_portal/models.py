from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


class IngredientCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ingredient Category"
        verbose_name_plural = "Ingredient Categories"


class Ingredient(models.Model):
    name = models.CharField(max_length=25, unique=True)
    category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name