from django import forms


from .models import Recipe

class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'href',
            'ingredients',
            'thumbnail'
        ]
