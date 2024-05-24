from .models import Recipe
from io import BytesIO
import base64
import matplotlib.pyplot as plt


# define a function that takes the ID
# def get_recipename_from_id(val):
#     recipename = Recipe.objects.get(id=val)
#     # and the name is returned back
#     return recipename


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    # return the image/graph
    return graph

# chart_type: user input o type of chart,
# data: pandas dataframe


def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')

    fig = plt.figure(figsize=(6, 3))

    # select chart_type based on user input from the form
    if chart_type == '#1':
        plt.bar(data['name'], data['cooking_time'])
        plt.xlabel("Name")
        plt.ylabel("Cooking Time")

    elif chart_type == '#2':
        labels = kwargs.get('labels')
        plt.pie(data['cooking_time'], labels=labels)
        plt.title("Recipe and Cooking Time")

    elif chart_type == '#3':
        plt.plot(data['name'], data['cooking_time'])
        plt.xlabel("Name")
        plt.ylabel("Cooking Time")

    else:
        print('unknown chart type')

    # specify layout details
    plt.tight_layout()

    # render the graph to file
    chart = get_graph()
    return chart