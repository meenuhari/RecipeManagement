from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from recipe.models import Recipe

from recipe.serializers import RecipeSerializer


# Create your views here.
class search(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if(query):
            recipes= Recipe.objects.filter(Q(name__icontains=query) | Q(ingredients__icontains=query))
            r=RecipeSerializer(recipes,many=True)
            return Response(r.data)
