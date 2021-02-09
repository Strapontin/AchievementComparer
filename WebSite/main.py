# venv\Scripts\activate
import urllib.request
from bs4 import BeautifulSoup
import threading


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Achievement:
    AchievementName = ""
    WholeDivHtml = ""


def get_header_to_link(html):
    for title in html.find_all('h3'):
        # Add a link to search on how to do the achievement
        link = BeautifulSoup().new_tag("a", href=f'http://www.google.com/search?q=halo+{title.string}+achievement')

        # Open in new tab on click
        link["target"] = "_blank"

        link.string = f'{title.string}'
        title.string.replace_with(link)

    return str(html)


# Get the player achievements from the player's achievement's URL
class get_achievements(threading.Thread):
    def __init__(self, link):
        super(get_achievements, self).__init__()
        self.link = link
        self.player_achievements = []

    def run(self):
        link_content = urllib.request.urlopen(self.link).read()

        # Get the content of the achievements of the 2 players
        personal_achieve = BeautifulSoup(link_content, 'html.parser').find(id='personalAchieve')

        # Get a list of all the achievements
        achievement_collection = personal_achieve.find_all(attrs={'class': 'achieveRow'})

        for a in achievement_collection:

            # If the player has unlocked the achievement, we add it in the list
            if 'achieveUnlockTime' in str(a):
                ach = Achievement()
                ach.AchievementName = a.find(attrs={'class': 'ellipsis'}).string
                ach.WholeDivHtml = get_header_to_link(a)

                self.player_achievements.append(ach)


# Gets the global Gameplay Stats for the game
class get_global_achievements(threading.Thread):
    def __init__(self, game_id):
        super(get_global_achievements, self).__init__()
        self.game_id = game_id
        self.all_achievements = []

    def run(self):
        link = f"https://steamcommunity.com/stats/{self.game_id}/achievements/"
        # link = "https://steamcommunity.com/stats/976730/achievements/"
        link_content = urllib.request.urlopen(link).read()

        # Gets the achievements
        personal_achieve = BeautifulSoup(link_content, 'html.parser').find(id='mainContents')
        achievement_collection = personal_achieve.find_all(attrs={'class': 'achieveRow'})

        for a in achievement_collection:
            ach = Achievement()
            ach.AchievementName = a.find(attrs={'class': 'achieveTxt'}).h3.string
            ach.WholeDivHtml = get_header_to_link(a)

            self.all_achievements.append(ach)


import datetime


# Press the green button in the gutter to run the script.
def show_achievements(game_id, player1, player2):
    link1 = f"https://steamcommunity.com/profiles/{player1}/stats/{game_id}/achievements?&l=en"
    link2 = f"https://steamcommunity.com/profiles/{player2}/stats/{game_id}/achievements?&l=en"

    date_start = datetime.datetime.now()

    # Get all the achievements for both players
    global_achievements_thread = get_global_achievements(game_id)
    achievements_p1_thread = get_achievements(link1)
    achievements_p2_thread = get_achievements(link2)

    # Start the threads
    global_achievements_thread.start()
    achievements_p1_thread.start()
    achievements_p2_thread.start()

    # Wait for all the threads to finish
    global_achievements_thread.join()
    achievements_p1_thread.join()
    achievements_p2_thread.join()

    # Get the data from the threads results
    global_achievements = global_achievements_thread.all_achievements

    achievements_p1 = achievements_p1_thread.player_achievements
    achievements_p2 = achievements_p2_thread.player_achievements

    achievements_p1_temp = achievements_p1.copy()

    date_end_thread = datetime.datetime.now()

    # For each achievement player 1 has, we search if player 2 has it also
    for achievement in achievements_p1_temp:

        # If both players have the achievement
        if any(achievement.AchievementName == a.AchievementName for a in achievements_p2):
            achievements_p1.remove(achievement)

            # Get and remove the achievement in player 2
            index_p2 = list(filter(lambda x: x.AchievementName == achievement.AchievementName, achievements_p2))
            achievements_p2.remove(index_p2[0])

    achievements_p1_temp += achievements_p2

    # Now we get all the achievements both players don't have
    for achievement in achievements_p1_temp:
        # Find the index of the achievement
        index = list(filter(lambda x: x.AchievementName == achievement.AchievementName, global_achievements))
        global_achievements.remove(index[0])

    x = []
    y = []
    z = []

    for a in achievements_p1:
        x.append(a.WholeDivHtml)

    for a in achievements_p2:
        y.append(a.WholeDivHtml)

    for a in global_achievements:
        z.append(a.WholeDivHtml)

    date_end = datetime.datetime.now()

    print(date_end_thread - date_start)
    print(date_end - date_start)

    return {"achievements_p1": x, "achievements_p2": y, "global_achievements": z}
