from django.shortcuts import render, redirect    # imported by default
# Displays list and details
from django.views.generic import ListView, DetailView
#import Recipe model
from .models import Recipe
# to protect class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
# to protect function-based views
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RecipesSearchForm, AddRecipeForm
import pandas as pd
from .utils import get_chart

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

def profile(request):
    return render(request, "recipes/profile.html")


class RecipeListView(LoginRequiredMixin, ListView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/recipes_list.html'  # specify template


class RecipeDetailView(LoginRequiredMixin, DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/details.html'  # specify template

# define function-based view - records(records()

# keep protected


@login_required
def records(request):
    # create an instance of RecipesSearchForm that you defined in recipes/forms.py
    form = RecipesSearchForm(request.POST or None)
    recipe_df = None  # initialize dataframe to None
    recipe_diff = None
    chart = None
    qs = None
    # check if the button is clicked
    if request.method == 'POST':
        recipe_diff = request.POST.get('recipe_diff')  # read recipe_name
        chart_type = request.POST.get('chart_type')  # read recipe chart type

        recipe_diff_data = {"#1": "Easy", "#2": "Medium",
                            "#3": "Intermediate", "#4": "Hard"}
        recipe_diff = recipe_diff_data[recipe_diff]

        qs = Recipe.objects.all()  # apply filter to extract data
        id_searched = []
        for obj in qs:
            diff = obj.calculate_difficulty()
            if diff == recipe_diff:
                id_searched.append(obj.id)

        qs = qs.filter(id__in=id_searched)

        if qs:  # if data found
            # convert the queryset values to pandas dataframe
            recipe_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipe_df,
                              labels=recipe_df['name'].values)

            # convert the dataframe to HTML
            recipe_df = recipe_df.to_html()

            for item in qs.values():
                item_id = item["id"]
                item_name = item["name"]
                recipe_df = recipe_df.replace(
                    f"<td>{item_name}</td>",
                    f'<td><a href = "/recipes/list/{item_id}">{item_name}</td>'
                )

    # print(recipe_df)
    # pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
        'recipe_df': recipe_df,
        'recipe_diff': recipe_diff,
        'chart': chart,
        'qs': qs,
    }
    # load the recipes/records.html page using the data that you just prepared
    return render(request, 'recipes/records.html', context)

@login_required
def add_recipe(request):
    print("add_recipe view function is called")
    if request.method == "POST":
        print("POST request received")
        create_form = AddRecipeForm(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, "Recipe created successfully.")
            return redirect('recipes:add_recipe')  # Corrected redirect name
    else:
        print("GET request received")
        create_form = AddRecipeForm()

    context = {"create_form": create_form}
    return render(request, "recipes/add_recipe.html", context)

