from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .forms import RecipeForm
import json
from django.contrib.auth.models import User
from . import models
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def recipe_handle(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            user_id = data.get('user_id')
             
            user = User.objects.get(id = user_id)

            recipe = models.Recipe.objects.create(recipe_name = data.get('name'),recipe_description = data.get('decription'), user=user)
            
            return JsonResponse({'status':'success','recipe_id': recipe.id},status=201)
        except User.DoesNotExist:
            return JsonResponse({'error':'User not found'},status=400)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=400)
    return JsonResponse({'error':'invalid error response'}, status=400)

def recipe_view(request):
    if request.method == 'GET':
        
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