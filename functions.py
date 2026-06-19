
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
con = m.connect(host="localhost", user="root", passwd="student", database="k2_26_27")
c = con.cursor()

failure = True
success = False

# Check for illegal content in input:
def illegal(tupl):
	for i in tupl:
		if not (i.replace(' ','').isalnum()):
			print("ERROR: Found illegal or no characters in input! Only include 0-9, a-z, A-Z .\nAborting...")
			print(i)
			return True
	return False


def add_team():
	tid = input("Enter Team ID: ").strip()
	tname = input("Eter Team Name: ")
	captain = input("Enter Captain's Name: ")
	
	if illegal((tid, tname, captain, )):
		return failure
	
	try:
		c.execute("INSERT Teams VALUES({}, '{}', '{}')".format(tid, tname, captain))
		print("Added Team '"+tname+"'.")
		return success
	except:
		print("ERROR: Failed to add team. Ensure you gave a valid integer Team ID.",)
	

def add_player():
	pid = input("Enter Player ID: ").strip()
	pname = input("Enter Player Name: ")
	tid = input("Enter Team ID: ").strip()
	role = input("Enter role: ")

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
	mid = input("Enter Match ID: ").strip()
	t1id = input("Enter Team1 ID: ").strip()
	t2id = input("Enter Team2 ID: ").strip()
	if t1id == t2id:
		print("ERROR: How can a team play against itself ? Team1 = Team2")
		return failure
	mdate = input("Enter Match Date in the format 'YYYY-MM-DD': ").strip()
	venue = input("Enter Venue: ")
	wid = input("Enter Winner Team ID: ").strip()
	if wid not in (t1id, t2id):
		print("ERROR: How can a team other than Team1 or Team2 be the winner ?\n(Winner != Team1 OR Winner != Team2)")
		return failure
	t1runs = input("Enter Team1 runs: ").strip()
	t2runs = input("Enter Team2 runs: ").strip()
	t1balls = input("Enter Team1 balls: ").strip()
	t2balls = input("Enter Team2 balls: ").strip()
	t1wickets = input("Enter Team1 wickets: ").strip()
	t2wickets = input("Enter Team2 wickets: ").strip()
	
	if illegal((mid, t1id, t2id, mdate.replace('-',''), venue, wid,\
				t1runs, t2runs, t1balls, t1wickets, t2wickets, )):
		return failure
	
	try: 
		c.execute("INSERT Matches VALUES({}, {}, {}, '{}', '{}', {}, {}, {}, {}, {}, {}, {})"\
					.format(mid, t1id, t2id, mdate, venue, wid, \
							t1runs, t2runs, t1balls, t2balls, t1wickets, t2wickets))
		print("Added match ID: "+mid+" held at "+venue+".")
		return failure
	except Exception as e:
		print("ERROR: Failed to add Match. Ensure you gave valid integers and correct Date format.",e)
		return failure 


def enter_scorecard():
		


	











	
