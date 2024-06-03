from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, records, profile, add_recipe

app_name = 'recipes'

urlpatterns = [
    #Home Page
    path('', home, name='home'),
    #List of recipes
    path('recipes/list/', RecipeListView.as_view(), name='list'),
    #Recipe details
    path('recipes/list/<pk>', RecipeDetailView.as_view(), name='detail'),
    #Search recipes
    path('recipes/search', records, name='records'),
    #Profile page
    path('recipes/profile', profile, name='profile'),
    #Adding recipes
    path('recipes/add_recipe', add_recipe, name='add_recipe')
]