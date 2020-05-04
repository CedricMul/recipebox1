from django.shortcuts import render, reverse, HttpResponseRedirect

from recipebox.models import Author, Recipe
from recipebox.forms import AuthorAddForm, RecipeAddForm
# Create your views here.
def index(request):
    author_data = Author.objects.all()
    recipe_data = Recipe.objects.all()
    return render(request, "index.html", {"author_data": author_data, "recipe_data": recipe_data })


def recipeadd(request):
    html = "recipe_add_form.html"
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect('/')

    else:
        form = RecipeAddForm()
    
    return render(request, html, {"form": form})


def authoradd(request):
    html = "author_add_form.html"
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio'],
            )
            return HttpResponseRedirect('/')

    else:
        form = AuthorAddForm()
    
    return render(request, html, {"form": form})


def author_detail(request, author_url):
    author_url = author_url.replace("_"," ").title()
    author = Author.objects.get(name=author_url)
    recipe_data = Recipe.objects.all()
    return render(request, "author_detail.html", {"author": author, "recipe_data": recipe_data})

def recipe_detail(request, recipe_url):
    recipe_url = recipe_url.replace("_"," ").title()
    recipe = Recipe.objects.get(title=recipe_url)
    return render(request, "recipe_detail.html", {"recipe": recipe})
