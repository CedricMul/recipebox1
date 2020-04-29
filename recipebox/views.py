from django.shortcuts import render, get_object_or_404

from recipebox.models import Author, Recipe
# Create your views here.
def index(request):
    author_data = Author.objects.all()
    recipe_data = Recipe.objects.all()
    return render(request, "index.html", {"author_data": author_data, "recipe_data": recipe_data })

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    recipe_data = Recipe.objects.all()
    return render(request, "author_detail.html", {"author": author, "recipe_data": recipe_data})

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, "recipe_detail.html", {"recipe": recipe})
