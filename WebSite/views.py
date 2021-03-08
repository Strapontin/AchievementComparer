from django.db.models.functions import Lower
from django.shortcuts import render, redirect
from .main import show_achievements
from . import models
from django.core import serializers


# Create your views here.
def show_players_achievements(request, game_id, player1, player2):
    achievements = show_achievements(game_id, player1, player2)
    return render(request, 'WebSite/home.html', context=achievements)


def redirect_to_default(request):
    game_halo = "976730"
    player_strapontin = "76561198086634382"
    player_sevenup = "76561198193278659"

    response = redirect(f'{game_halo}/{player_strapontin}/{player_sevenup}/')
    return response


def edit(request, game_id, player1, player2):
    context = {"game_id": game_id, "player1": player1, "player2": player2}

    response = render(request, 'WebSite/edit.html', context=context)
    return response


def find_games(request):
    game_title = request.GET['gameName']

    games = models.Games.objects.filter(name__startswith=game_title).order_by(Lower('name'))[:100]
    games = serializers.serialize("python", games)

    return render(request, 'WebSite/games_list.html', {
        'games': games
    })
