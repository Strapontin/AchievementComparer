from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^(?P<game_id>[0-9]+)/(?P<player1>[0-9]+)/(?P<player2>[0-9]+)/$', views.show_players_achievements, name='home'),
    path('', views.redirect_to_default, name='redirect'),
    re_path(r'^(?P<game_id>[0-9]+)/(?P<player1>[0-9]+)/(?P<player2>[0-9]+)/edit$', views.edit, name='edit'),
    path('ajax/find_games', views.find_games, name='find_games'),
]
