from django.shortcuts import render
from .main import show_achievements


# Create your views here.
def show_players_achievements(request):
    achievements = show_achievements()
    return render(request, 'WebSite/home.html', context=achievements)
