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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    link1 = "https://steamcommunity.com/profiles/76561198086634382/stats/976730/achievements?&l=en"
    link2 = "https://steamcommunity.com/profiles/76561198193278659/stats/976730/achievements?&l=en"

    # Get all the achievements for both players
    achievementsP1 = get_achievements(link1)
    achievementsP2 = get_achievements(link2)

    achievementsP1Temp = achievementsP1.copy()

    # For each achievement player 1 has, we search if player 2 has it also
    for achievement in achievementsP1Temp:
        if any(achievement.AchievementName == a.AchievementName for a in achievementsP2):
            achievementsP1.remove(achievement)

            # Get and remove the achievement in player 2
            indexP2 = list(filter(lambda x: x.AchievementName == achievement.AchievementName, achievementsP2))
            achievementsP2.remove(indexP2[0])

    print([a.AchievementName for a in achievementsP1])
    print([a.AchievementName for a in achievementsP2])

