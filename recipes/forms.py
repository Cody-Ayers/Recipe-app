from django import forms  # import django forms

CHART__CHOICES = (  # specify choices as a tuple
    # when user selects "Bar chart", it is stored as "#1"
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

DIFFIC__CHOICES = (  # specify choices as a tuple
    # when user selects "Easy", it is stored as "#1"
    ('#1', 'Easy'),
    ('#2', 'Medium'),
    ('#3', 'Intermediate'),
    ('#4', 'Hard')
)

# define class-based Form imported from Django forms


class RecipesSearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFFIC__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)