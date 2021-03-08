from django.db import models, transaction
import urllib.request
import json
import time


# Create your models here.
class Games(models.Model):
    appId = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# models.Games.objects.filter(name__startswith='test')
def get_all_games():
    with urllib.request.urlopen("https://api.steampowered.com/ISteamApps/GetAppList/v2/") as f:
        # start_time = time.time()
        games_content = json.loads(f.read())
        games_list = games_content['applist']['apps']

        # Delete all data as we're loading it back in
        Games.objects.all().delete()
        # print("--- %s seconds ---" % (time.time() - start_time))

        # start_time = time.time()
        with transaction.atomic():
            for game in games_list:
                Games(appId=game['appid'], name=game['name']).save()

        # print("--- %s seconds ---" % (time.time() - start_time))
