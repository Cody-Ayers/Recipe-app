from django.urls import path
from .views import home, RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    # THis takes you to home page
    path('home/', home, name='home'),
    # These next two shows you the list of recipes and the details note need to use .as_view()
    path('recipes/list/', RecipeListView.as_view(), name='list'),
    # note need to use .as_view(), which returns callable view that takes a request and returns the response
    path('recipes/list/<pk>', RecipeDetailView.as_view(), name='detail'),
]