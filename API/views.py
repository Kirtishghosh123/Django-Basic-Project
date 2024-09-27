from django.shortcuts import render, redirect
from rest_framework.views import APIView
import json
from django.contrib.auth.models import User
from . import models
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from . import serializers
from django.views import View
from django.contrib.auth import authenticate, login
from rest_framework.decorators import permission_classes
# Create your views here.
class Login(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        user = request.user 
        return JsonResponse({'status': 'success', 'user': user.username}, status=status.HTTP_200_OK)
   
class Homeview(View):
    permission_classes = [AllowAny]

    def get(self,request):
        return render(request,'home.html')
    

    


class Recipe(APIView):
    def post(self,request):
            if request.method == 'POST':
                try:
                    data = json.loads(request.body)

                    user_id = data.get('user_id')
                    
                    user = User.objects.get(username = user_id)

                    recipe = models.Recipe.objects.create(recipe_name = data.get('name'),recipe_description = data.get('description'), user=user)
                    
                    return JsonResponse({'status':'success','recipe_id': recipe.id},status=201)
                except User.DoesNotExist:
                    return JsonResponse({'error':'User not found'},status=400)
                except Exception as e:
                    return JsonResponse({'error':str(e)},status=400)
            return JsonResponse({'error':'invalid error response'}, status=400)

class RecipeView(APIView):
    def get(self,request):    
                recipes = models.Recipe.objects.all()
                recipe_list = []
                for i in recipes:
                    recipe_list.append(
                        {
                            'name': i.recipe_name,
                            'description': i.recipe_description,
                            'user': i.user.username
                        }
                    )
                return JsonResponse(recipe_list, status=200, safe=False)
            

class RegisterView(APIView):
    
    def get(self, request):
        serializer = serializers.UserSerializer
        return render(request, 'register.html')
    
    def post(self, request):
        try:
            serializer = serializers.UserSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.save()
                return JsonResponse({'status':'success',
                                               'refresh':data['refresh'],
                                               'access': data['access_token'],
                                               'username':data['username']
                                               }, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'error':str(serializer.error_messages)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return JsonResponse({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
