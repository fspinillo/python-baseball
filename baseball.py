import datetime
import urllib2
import json

now = datetime.datetime.now()
gameday_url = "http://gd2.mlb.com/components/game/mlb/year_%d/month_%s/day_%s/miniscoreboard.json" \
				% (now.year, now.strftime("%m"), now.strftime("%d"))

gameday_response = urllib2.urlopen(gameday_url)
gameday_data = json.load(gameday_response)
games_array = gameday_data['data']['games']['game']

for game in games_array:
	if 'home_team_runs' in game:
		print '%s (%s) vs %s (%s) @ %s' % (game['away_team_name'], game['away_team_runs'], \
			game['home_team_name'], game['home_team_runs'], game['venue'])
	else:
		print '%s vs %s @ %s %s' % (game['away_team_name'], game['home_team_name'], game['venue'], game['time'])