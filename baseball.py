from datetime import datetime, timedelta
import requests
import json

#function to determine the status of a game, if no team selected
#based on the progress, different data is returned

def game_info():
    if game['status']['status'] == "In Progress":
        return '%s (%s) vs %s (%s) @ %s %s' % (
                game['away_team_name'],
                game['linescore']['r']['away'],
                game['home_team_name'],
                game['linescore']['r']['home'],
                game['venue'],
                game['status']['status']
            )
    elif (game['status']['status'] == "Final" or game['status']['status'] == "Game Over"):
        return '%s (%s) vs %s (%s) @ %s %s' % (
                game['away_team_name'],
                game['linescore']['r']['away'],
                game['home_team_name'],
                game['linescore']['r']['home'],
                game['venue'],
                game['status']['status']
            )
    elif (game['status']['status'] == "Pre-Game" or game['status']['status'] == "Preview"):
        return '%s vs %s @ %s %s%s %s' % (
                game['away_team_name'],
                game['home_team_name'],
                game['venue'],
                game['home_time'],
                game['hm_lg_ampm'],
                game['status']['status']
            )

#function to determine the status of a game, if a team is selected
#based on the progress, different data is returned

def team_score():
    if game['status']['status'] == "In Progress":
        return \
        '-------------------------------\n' \
        '%s (%s) vs. %s (%s) @ %s\n' \
        '%s: %s of the %s\n' \
        'Pitching: %s || Batting: %s || S: %s B: %s O: %s\n' \
        '-------------------------------' % (
                game['away_team_name'],
                game['linescore']['r']['away'],
                game['home_team_name'],
                game['linescore']['r']['home'],
                game['venue'],
                game['status']['status'],
                game['status']['inning_state'],
                game['status']['inning'],
                game['pitcher']['last'],
                game['batter']['last'],
                game['status']['s'],
                game['status']['b'],
                game['status']['o']
            )
    elif (game['status']['status'] == "Final" or game['status']['status'] == "Game Over"):
        return \
        '-------------------------------\n' \
        '%s (%s) vs. %s (%s) @ %s\n' \
        'W: %s || L: %s || SV: %s\n' \
        '-------------------------------' % (
                game['away_team_name'],
                game['linescore']['r']['away'],
                game['home_team_name'],
                game['linescore']['r']['home'],
                game['venue'],
                game['winning_pitcher']['name_display_roster'],
                game['losing_pitcher']['name_display_roster'],
                game['save_pitcher']['name_display_roster']
            )
    elif (game['status']['status'] == "Pre-Game" or game['status']['status'] == "Preview"):
        return \
        '-------------------------------\n' \
        '%s vs %s @ %s %s%s\n' \
        'P: %s || P: %s\n' \
        '-------------------------------' % (
                game['away_team_name'],
                game['home_team_name'],
                game['venue'],
                game['home_time'],
                game['hm_lg_ampm'],
                game['away_probable_pitcher']['name_display_roster'],
                game['home_probable_pitcher']['name_display_roster']
               )

#function to determine which feed to grab based on user input

def date_url(date):
    if date == "yesterday":
        baseball_url = "http://gd2.mlb.com/components/game/mlb/year_%d/month_%s/day_%s/master_scoreboard.json" \
        % (now.year, now.strftime("%m"), yesterday.strftime("%d"))
    else:
        baseball_url = "http://gd2.mlb.com/components/game/mlb/year_%d/month_%s/day_%s/master_scoreboard.json" \
                % (now.year, now.strftime("%m"), now.strftime("%d"))
    return baseball_url

#process to set date, and convert if need be.

now = datetime.now()
yesterday = datetime.now() - timedelta(days=1)
date = raw_input('Today or yesterday? ').lower()

#builds the data structure from the feed

baseball_data = requests.get(date_url(date))
game_data = baseball_data.json()
game_array = game_data['data']['games']['game']

team = raw_input('What team do you want? ex. SF or NYY ').upper()

for game in game_array:
    if team == "":
        disp = game_info()
        if disp:
            print disp
    else:
        if (game['home_name_abbrev']) == team or (game['away_name_abbrev']) == team:
            disp = team_score()
            if disp:
                print disp
