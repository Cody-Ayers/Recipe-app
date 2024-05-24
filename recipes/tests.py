from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm
# Create your tests here.
class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name='banana smoothie', cooking_time=7, ingredients='bananas, strawberries, honey, ice cubes, yogurt',
                              description='Chop up banana and strawberries and add them to the blender along with your cup of ice cubes.  Next add your yogurt and  a few teaspoons of honey. Once everything is in the container blend until desired thickness')

    def test_desciption(self):
        recipe = Recipe.objects.get(id=1)
        name_max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(name_max_length, 50)

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name_label, 'name')

    def test_cookingtime_helptext(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cookingtime = recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(recipe_cookingtime, 'minutes')

    def test_difficulty_calculation(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.calculate_difficulty(), 'Medium')

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/recipes/list/1')

class RecipeSearchFormTest(TestCase):

    def test_form_renders_recipe_diff_input(self):
        form = RecipesSearchForm()
        self.assertIn('recipe_diff', form.as_p())

    def test_form_renders_chart_type_input(self):
        form = RecipesSearchForm()
        self.assertIn('chart_type', form.as_p())

    def test_form_valid_data(self):
        form = RecipesSearchForm(
            data={'recipe_diff': '#1', 'chart_type': '#2'})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = RecipesSearchForm(data={'recipe_diff': '', 'chart_type': ''})
        self.assertFalse(form.is_valid())