from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from recipebox.models import Author, Recipe
from recipebox.forms import AuthorAddForm, RecipeAddForm, LoginForm, RecipeModelForm

# Create your views here.
def index(request):
    author_data = Author.objects.all()
    recipe_data = Recipe.objects.all()
    return render(request, "index.html", {"author_data": author_data, "recipe_data": recipe_data })


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request, "signup_form.html", {"form": form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "signup_form.html",
                  context={"form":form})


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username = data['username'], password = data['password']
                )
            if user:
                login(request, user)
                
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'login_form.html', {'form': form})


def logoutview(request):
    logout(request)
    messages.info(request, "Logged out!")
    return HttpResponseRedirect(reverse('homepage'))


@login_required
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
            return HttpResponseRedirect(reverse('homepage'))

    else:
        form = RecipeAddForm()
    
    return render(request, html, {"form": form})


@staff_member_required
def authoradd(request):
    html = "author_add_form.html"
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio'],
                user=data['user']
            )
            return HttpResponseRedirect(reverse('homepage'))

    else:
        form = AuthorAddForm()
    
    return render(request, html, {"form": form})

def recipe_edit_view(request, id):
    recipe = Recipe.objects.get(id=id)
    populated_form = RecipeModelForm(request.POST, instance=recipe)
    return render(request, 'recipe_add_form.html', {"recipe": populated_form})

def author_detail(request, author_url):
    author_url = author_url.replace("_"," ").title()
    author = Author.objects.get(name=author_url)
    recipe_data = Recipe.objects.all()
    return render(request, "author_detail.html", {"author": author, "recipe_data": recipe_data})

def recipe_detail(request, recipe_url):
    recipe_url = recipe_url.replace("_"," ").title()
    recipe = Recipe.objects.get(title=recipe_url)
    return render(request, "recipe_detail.html", {"recipe": recipe})
