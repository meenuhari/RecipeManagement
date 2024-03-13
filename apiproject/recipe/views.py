from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer
from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from recipe.serializers import UserSerializer
from recipe.models import Review
from recipe.serializers import ReviewSerializer




# Create your views here.

#1.
class RecipeView(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
#2.filter recipe according to mealtype

class Recipelist(APIView):
    def get(self,request):

            recipes= Recipe.objects.filter(Q(cuisine__icontains='main dish ') | Q(ingredients__icontains='Rice'))
            r=RecipeSerializer(recipes,many=True)
            return Response(r.data)


#3.User Authentication
class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =UserSerializer

#4
class user_logout(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
#5.Review
class ReviewAll(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
