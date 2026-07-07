
#START:

from functions import * 

def main():
	
	while True:
		ch = get_choice()
		
		if ch == '0':
			continue
		elif ch == '1':
			add_team()
		elif ch == '2':
			add_player()
		elif ch == '3':
			create_match()
		elif ch == '4':
			enter_scorecard()
		elif ch == '5':
			match_summary()
		elif ch == '6':
			team_stats()
		elif ch == '7':
			player_stats()
	
	pass



main()

#END: 
con.commit()
con.close()
