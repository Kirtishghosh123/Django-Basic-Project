from django import forms
from .models import Recipe
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name','recipe_description']
        # exclude = ['user']
