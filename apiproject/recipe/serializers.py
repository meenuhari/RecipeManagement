from django.contrib.auth.models import User
from rest_framework import serializers

from recipe.models import Recipe

from recipe.models import Review




class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['id','name','cuisine','meal_type','ingredients']

class UserSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password']
    def create(self,validated_data):
        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['recipe','user','comment','reviewed_at']

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['recipe','user','rating','reviewed_at']