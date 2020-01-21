from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ( 
    			'title',
    			'ingredients',
    			'href',
				'thumbnail',
            	)

    odering = ['title']
    search_fields = ('href', 'title')


admin.site.register(Recipe, RecipeAdmin)

# Register your models here.
