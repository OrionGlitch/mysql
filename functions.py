
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
con = m.connect(host="localhost", user="root", passwd="student", database="cricket")
c = con.cursor()

failure = True
success = False

# Check for illegal content in input:
def illegal(lst):
	for i in range(len(lst)):
		if lst[i] == "":
			lst[i] = "NULL"
		elif lst[i] == "NULL":
			pass 
		elif not (lst[i].replace(' ','').isalnum()):
			print("ERROR: Found illegal or no characters in input! Only include 0-9, a-z, A-Z .\nAborting...")
			return True
	return False


def add_team():
	tid = input("Enter Team ID: ").strip()
	tname = input("Eter Team Name: ").strip()
	captain = input("Enter Captain's Name: ").strip()
	
	if illegal((tid, tname, captain, )):
		return failure
	
	try:
		c.execute("INSERT Teams VALUES({}, '{}', '{}')".format(tid, tname, captain))
		print("Added Team '"+tname+"'.")
		return success
	except:
		print("ERROR: Failed to add team. Ensure you gave a valid integer Team ID.",)
		return failure
	

def add_player():
	pid = input("Enter Player ID: ").strip()
	pname = input("Enter Player Name: ").strip()
	tid = input("Enter Team ID: ").strip()
	role = input("Enter role: ").strip()

	if illegal((pid, pname, tid, role, )):
		return failure
	
	try:
		c.execute("INSERT Players VALUES({},'{}',{},'{}')".format(pid, pname, tid, role))
		print("Added player '"+pname+"'.")
		return success
	except:
		print("ERROR: Failed to add Player. Ensure you gave a valid integer for Team ID and Player ID.")
		return failure


def create_match():
	dic = {}
	dic['mid'] = input("Enter Match ID: ").strip()
	dic['tid'] = input("Enter Team1 ID: ").strip()
	dic['t2id'] = input("Enter Team2 ID: ").strip()
	if dic['tid'] == dic['t2id']:
		print("ERROR: How can a team play against itself ? Team1 = Team2")
		return failure
	dic['mdate'] = input("Enter Match Date in the format 'YYYY-MM-DD': ").strip()
	dic['venue'] = input("Enter Venue: ").strip()
	dic['wid'] = input("Enter Winner Team ID: ").strip()
	if wid not in (t1id, t2id):
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
		c.execute("INSERT Matches VALUES({}, {}, {}, '{}', '{}', {}, {}, {}, {}, {}, {}, {})"\
					.format(dic['mid'], dic['t1id'], dic['t2id'], dic['mdate'], dic['venue'], dic['wid'], \
							dic['t1runs'], dic['t2runs'], dic['t1balls'], dic['t2balls'], \
							dic['t1wickets'], dic['t2wickets']))
		print("Added match ID: "+dic['mid']+" held at "+dic['venue']+".")
		return success
	except:
		print("ERROR: Failed to add Match. Ensure you gave valid integers and correct Date format.")
		return failure 


def enter_scorecard():
	dic = {}
	dic['mid'] = input("Enter Match ID: ").strip()
	dic['pid'] = input("Enter Player ID: ").strip()
	dic['tid'] = input("Enter Team ID: ").strip()
	dic['runs'] = input("Enter Runs: ").strip()
	dic['balls'] = input("Enter Balls: ").strip()
	dic['fours'] = input("Enter Fours: ").strip()
	dic['sixes'] = input("Enter Sixes: ").strip()
	dic['wicks'] = input("Enter No. of Wickets: ").strip()
	
	if illegal(dic):
		return failure
	
	try:
		c.execute("INSERT Scorecard VALUES({}, {}, {}, {}, {}, {}, {}, {})"\
				   .format(dic['mid'], dic['pid'], dic['tid'], dic['runs'],\
				    dic['balls'], dic['fours'], dic['sixes'], dic['wicks']))
		print("Added Scorecard for Match ID: "+mid+" by player ID: "+pid+".")
		return success
	except Exception as e:
		print("ERROR: Failed to add Scorecard. Ensure you gave valid integers.", e)
		return failure 



	











	
