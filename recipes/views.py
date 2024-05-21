from django.shortcuts import render    # imported by default
# Displays list and details
from django.views.generic import ListView, DetailView
# This will access Recipe model
from .models import Recipe
# to protect class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
# to protect function-based views
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'recipes/recipes_home.html')


class RecipeListView(LoginRequiredMixin, ListView):  #class-based "protected" view
    model = Recipe                                   #specify model
    template_name = 'recipes/recipes_list.html'      #specify template

class RecipeDetailView (DetailView):                 #class-based "protected" view
    model = Recipe                                   #specify model
    template_name = 'recipes/details.html'           #specify template
