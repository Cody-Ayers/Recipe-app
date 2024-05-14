from django.test import TestCase
from .models import Recipe

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
