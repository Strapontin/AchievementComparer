# This is a sample Python script.
import urllib.request
from bs4 import BeautifulSoup


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Achievement:
    AchievementName = ""
    WholeDivHtml = ""


# Get the player achievements from the player's achievement's URL
def get_achievements(link):
    link_content = urllib.request.urlopen(link).read()

    # Get the content of the achievements of the 2 players
    personal_achieve = BeautifulSoup(link_content, 'html.parser').find(id='personalAchieve')

    # Get a list of all the achievements
    achievement_collection = personal_achieve.find_all(attrs={'class': 'achieveRow'})

    player_achievements = []

    for a in achievement_collection:

        # If the player has unlocked the achievement, we add it in the list
        if 'achieveUnlockTime' in str(a):
            ach = Achievement()
            ach.AchievementName = a.find(attrs={'class': 'ellipsis'}).string
            ach.WholeDivHtml = str(a)

            player_achievements.append(ach)

    return player_achievements


# Gets the global Gameplay Stats for the game
def get_global_achievements():
    link = "https://steamcommunity.com/stats/976730/achievements/"
    link_content = urllib.request.urlopen(link).read()

    # Gets the achievements
    personal_achieve = BeautifulSoup(link_content, 'html.parser').find(id='mainContents')
    achievement_collection = personal_achieve.find_all(attrs={'class': 'achieveRow'})

    all_achievements = []

    for a in achievement_collection:
        ach = Achievement()
        ach.AchievementName = a.find(attrs={'class': 'achieveTxt'}).h3.string
        ach.WholeDivHtml = str(a)

        all_achievements.append(ach)

    return all_achievements


# Press the green button in the gutter to run the script.
def show_achievements():

    link1 = "https://steamcommunity.com/profiles/76561198086634382/stats/976730/achievements?&l=en"
    link2 = "https://steamcommunity.com/profiles/76561198193278659/stats/976730/achievements?&l=en"

    global_achievements = get_global_achievements()

    # Get all the achievements for both players
    achievements_p1 = get_achievements(link1)
    achievements_p2 = get_achievements(link2)

    achievements_p1_temp = achievements_p1.copy()

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

    print("nb achievements")
    print(len(global_achievements))

    x = []
    y = []
    z = []

    for a in achievements_p1:
        x.append(a.WholeDivHtml)

    for a in achievements_p2:
        y.append(a.WholeDivHtml)

    for a in global_achievements:
        z.append(a.WholeDivHtml)

    return {"achievements_p1": x, "achievements_p2": y, "global_achievements": z}
