from django.shortcuts import render, redirect
from .main import show_achievements


# Create your views here.
def show_players_achievements(request, game_id, player1, player2):
    achievements = show_achievements(game_id, player1, player2)
    return render(request, 'WebSite/home.html', context=achievements)


def redirect_to_default(request):
    response = redirect('976730/76561198086634382/76561198193278659/')
    return response
