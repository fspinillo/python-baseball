import datetime
import urllib2
import json

# Procedure checks the team input for scores first.
# If scores is true, then it prints info for all the games.
# If a team abbreviation is true, it prints the game info only for that game.

def team_score(t):
	if t == 'scores':
		print '%s (%s) vs %s (%s) @ %s' % (game['away_team_name'], game['away_team_runs'], \
			game['home_team_name'], game['home_team_runs'], game['venue'])
	elif (game['home_file_code']) == team or (game['away_code']) == t:
			team_scores = '%s (%s) vs %s (%s) @ %s' % (game['away_team_name'], game['away_team_runs'], \
			game['home_team_name'], game['home_team_runs'], game['venue'])
			print team_scores

# Procedure checks the same as above, except this is used if the game has not started yet.

def team_pending(t):
	if t == 'scores':
		print '%s vs %s @ %s %s' % (game['away_team_name'], game['home_team_name'], game['venue'], game['time'])
	elif (game['home_file_code']) == team or (game['away_code']) == t:
		team_pending_info = '%s vs %s @ %s %s' % (game['away_team_name'], game['home_team_name'], game['venue'], game['time'])
		print team_pending_info

# Requests the type of score information from the user.

print "Please enter the name of the team you want scores for.", '\n' \
		"ex: nyy, sfn, la, etc.", '\n' \
		"If you just want all the scores, enter scores."

team = raw_input('Which team shall it be?: ')

# Captures the current date, and appends it to the base url for the data.

now = datetime.datetime.now()
gameday_url = "http://gd2.mlb.com/components/game/mlb/year_%d/month_%s/day_%s/miniscoreboard.json" \
				% (now.year, now.strftime("%m"), now.strftime("%d"))

# Pulls the json info into urllib2 and creates the array for the procedures

gameday_response = urllib2.urlopen(gameday_url)
gameday_data = json.load(gameday_response)
games_array = gameday_data['data']['games']['game']

#calls the procedures based on if the game has started or not

for game in games_array:
	if 'home_team_runs' in game:
		team_score(team)
	else:
		team_pending(team)