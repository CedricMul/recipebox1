from django.shortcuts import render, get_object_or_404

from recipebox.models import Author, Recipe
# Create your views here.
def index(request):
    author_data = Author.objects.all()
    recipe_data = Recipe.objects.all()
    return render(request, "index.html", {"author_data": author_data, "recipe_data": recipe_data })

def author_detail(request, author_url):
    author_url = author_url.replace("-"," ").title()
    author = Author.objects.get(name=author_url)
    recipe_data = Recipe.objects.all()
    return render(request, "author_detail.html", {"author": author, "recipe_data": recipe_data})

def recipe_detail(request, recipe_url):
    recipe_url = recipe_url.replace("-"," ").title()
    recipe = Recipe.objects.get(title=recipe_url)
    return render(request, "recipe_detail.html", {"recipe": recipe})
