from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_players_achievements, name='home'),
    # path('test/', views.test, name='test')
]
