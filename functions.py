
#MENU:
#	ADD TEAM
# 	ADD PLAYER
# 	CREATE MATCH
# 	ENTER SCORECARD
# 	VIEW MATCH SUMMARY
# 	TOP RUN SCORERS
# 	TOP WICKET TAKERS
# 	EXIT

import mysql.connector as m
from summarize_functions import *
con = m.connect(host="localhost", user="root", passwd="student", database="cricket")
c = con.cursor()

failure = True
success = False

# Check for illegal content in input:
def illegal(dic):
	for i in dic:
		if dic[i] == "":
			dic[i] = "NULL"
		elif dic[i] == "NULL":
			pass 
		elif not (dic[i].replace(' ','').replace('-','').isalnum()):
			print("ERROR: Found illegal or no characters in input! Only include 0-9, a-z, A-Z .\nAborting...")
			return True
	return False


def add_team():
	dic = {}
	print("ADD NEW TEAM\n============")
	dic["tname"] = input("Enter Team Name: ").strip().upper()
	dic["captain"] = input("Enter Captain's Name: ").strip().capitalize()
	
	if illegal(dic):
		return failure
	
	try:
		c.execute("INSERT Teams VALUES('{}', '{}')".format(dic['tname'], dic['captain']))
		print("Added Team '"+dic["tname"]+"'.")
		return success
	except Exception as e:
		print("ERROR: Failed to add team. Ensure you gave a valid integer Team ID.",e)
		return failure
	

def add_player():
	dic = {}
	print("ADD NEW PLAYER:\n===============")
	dic["pid"] = input("Enter Player ID: ").strip()
	dic["pname"] = input("Enter Player Name: ").strip().capitalize()
	dic["tname"] = input("Enter Team Name: ").strip().upper()
	dic["role"] = input("Enter role: ").strip().capitalize()

	if illegal(dic):
		return failure
	
	try:
		c.execute("INSERT Players VALUES({},'{}','{}','{}')".format(dic["pid"], dic["pname"], dic["tname"], dic["role"]))
		print("Added player '"+dic["pname"]+"'.")
		return success
	except Exception as e:
		print("ERROR: Failed to add Player. Ensure you gave a valid integer for Team ID and Player ID.",e)
		return failure


def create_match():
	dic = {}
	print("CREATE NEW MATCH:\n=================")
	dic['mid'] = input("Enter Match ID: ").strip()
	dic['t1name'] = input("Enter Team1 Name: ").strip().upper()
	dic['t2name'] = input("Enter Team2 Name: ").strip().upper()
	if dic['t1name'] == dic['t2name']:
		print("ERROR: How can a team play against itself ? Team1 = Team2")
		return failure
	dic['mdate'] = input("Enter Match Date in the format 'YYYY-MM-DD': ").strip()
	dic['venue'] = input("Enter Venue: ").strip()
	dic['wname'] = input("Enter Winner Team Name: ").strip().upper()
	if dic['wname'] not in (dic['t1name'], dic['t2name']):
		print("ERROR: How can a team other than Team1 or Team2 be the winner ?\n(Winner != Team1 OR Winner != Team2)")
		return failure
	dic['t1runs'] = input("Enter Team1 runs: ").strip()
	dic['t2runs'] = input("Enter Team2 runs: ").strip()
	dic['t1balls'] = input("Enter Team1 balls: ").strip()
	dic['t2balls'] = input("Enter Team2 balls: ").strip()
	dic['t1wickets'] = input("Enter Team1 wickets: ").strip()
	dic['t2wickets'] = input("Enter Team2 wickets: ").strip()
	
	if illegal(dic):
		return failure
	
	try: 
		c.execute("INSERT Matches VALUES({}, '{}', '{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {})"\
					.format(dic['mid'], dic['t1name'], dic['t2name'], dic['mdate'], dic['venue'], dic['wname'], \
							dic['t1runs'], dic['t2runs'], dic['t1balls'], dic['t2balls'], \
							dic['t1wickets'], dic['t2wickets']))
		print("Added match ID: "+dic['mid']+" held at "+dic['venue']+".")
		return success
	except Exception as e:
		print("ERROR: Failed to add Match. Ensure you gave valid integers and correct Date format.",e)
		return failure 


def enter_scorecard():
	dic = {}
	print("ENTER SCORECARD:\n================")
	dic['mid'] = input("Enter Match ID: ").strip()
	dic['pid'] = input("Enter Player ID: ").strip()
	dic['tname'] = input("Enter Team Name: ").strip()
	dic['runs'] = input("Enter Runs: ").strip()
	dic['balls'] = input("Enter Balls: ").strip()
	dic['fours'] = input("Enter Fours: ").strip()
	dic['sixes'] = input("Enter Sixes: ").strip()
	dic['wicks'] = input("Enter No. of Wickets: ").strip()
	
	if illegal(dic):
		return failure
	
	try:
		c.execute("INSERT Scorecard VALUES({}, {}, '{}', {}, {}, {}, {}, {})"\
				   .format(dic['mid'], dic['pid'], dic['tname'], dic['runs'],\
				    dic['balls'], dic['fours'], dic['sixes'], dic['wicks']))
		print("Added Scorecard for Match ID: "+dic["mid"]+" by player ID: "+dic["pid"]+".")
		return success
	except Exception as e:
		print("ERROR: Failed to add Scorecard. Ensure you gave valid integers.", e)
		return failure 


def get_choice():
	print("-_" * 50)
	print("OPTIONS:\n\t1. Add New Team.\n\t2. Add New Player.\n\t3. Add New Match.\n\t"+\
		  "4. Enter Scorecard of a Player in a Match.\n\t5. View a Match Summary.\n\t"+\
		  "6. Show Team Stats.\n\t7. Show Player Stats.\n\t")
	ch = input("Enter choice [1-7]: ")
	if ch not in ('1', '2', '3', '4', '5', '6', '7'):
		print("Invalid choice. Please enter a choice in range [1-7].")
		return '0'
	return ch

def match_summary():
	print("MATCH SUMMARY:\n==============")
	mid = input("Enter Match ID (or simply press Enter if don't know):").strip()
	if mid == "":
		t1name = input("Enter Team1 Name: ").strip()
		t2name = input("Enter Team2 Name (or simply press Enter if don't know): ").strip()
		if illegal({0:t1name, 2:t2name}):
			return 
		if t2name == "":
			c.execute("SELECT * FROM Matches WHERE team1_name='{}' OR team2_name='{}'".format(t1name,t1name))
			r = c.fetchall()
		else:
			c.execute("SELECT * FROM Matches WHERE (team1_name='{}' AND team2_name='{}') OR \
					   (team1_name='{}' AND team2_name='{}')"\
					   .format(t1name,t2name, t2name, t1name))
			r = c.fetchall()
	else:
		if not mid.isdigit():
			print("ERROR: Match ID Must be an integer.")
			return 
		c.execute("SELECT * FROM Matches WHERE match_id={}".format(mid))
		r = c.fetchall()
	if r == []:
		print("No Matches Found !")
		return 
	l = len(r)
	if l == 1:
		summarize_match(r[0])
	else:
		print("Found {} possible matches. Choose one:".format(l))
		for i in range(l):
			print("\t{}. MID({}): {} V/S {} on '{}' at {}.".format(i, r[i][0], r[i][1], r[i][2], r[i][3], r[i][4]))
		ch = input("Enter a choice [0-{}]:".format(l-1))
		if not ch.isdigit():
			print("ERROR: Give a valid integer.")
			return
		ch = int(ch)  
		if ch not in range(l):
			print("ERROR: Give a input in range [0-{}].".format(l-1))
			return 
		summarize_match(r[ch])
		
def team_stats():
	tname = input("Enter Team Name: ").strip()
	if illegal({0:tname}):
		return failure 
	
	c.execute("SELECT * FROM Teams WHERE team_name='{}'".format(tname))
	rteam = c.fetchall()
	if rteam == []:
		print("No Such Team Found!")
		return 
	c.execute("SELECT * FROM Players WHERE team_name='{}'".format(tname))
	rplayers = c.fetchall()
	c.execute("SELECT * FROM Matches WHERE team1_name='{}' OR team2_name='{}'".format(tname,tname))
	rmatches = c.fetchall()
	
	summarize_team(rteam, rplayers, rmatches)


def player_stats():
	pid = input("Enter Player ID (or leave empty if don't know): ").strip()
	if pid == "":
		pname = input("Enter Player Name: ").strip()
		if illegal({0:pname}):
			return failure 
		c.execute("SELECT * FROM Players WHERE player_name='{}'".format(pname))
		r = c.fetchall()
	else:
		if not pid.isdigit():
			print("ERROR: Please provide a valid integer for Player ID.")
			return failure
		c.execute("SELECT * FROM Players WHERE player_id={}".format(pid))
		r = c.fetchall()
	
	if r == []:
		print("No Such Player Found!")
		return 
	l = len(r)
	if l > 1:
		print("Muliple Players found with same Name. Select any One:")
		for i in range(l):
			print("{} PID({}): {} from team {}.".format(i,r[i][0], r[i][1], r[i][2]))
		ch = input("Enter a choice [0-{}]:".format(l-1))
		if not ch.isdigit():
			print("ERROR: Give an integer input. ")
			return failure
		ch = int(ch)
		if ch not in range(l):
			print("Please give a choice in [0-{}].".format(l-1))
			return failure 
	else:
		ch = 0
	c.execute("SELECT * FROM Scorecard WHERE player_id={}".format(r[ch][0]))
	rscorecards = c.fetchall()
	
	summarize_player(r[ch], rscorecards)
		
	

















	
