#There are two basketball teams (Team1 and Team2) in a school and they play some matches everyday depending on their time and interest. 
#Some days they play 3 matches, some days 2, some days 1 etc.

#Write a python function, find_winner_of_the_day(), which accepts the name of the winner of each match and returns the name of the overall winner of the day. 
#In case of equal number of wins, return “Tie”.

#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    team1_count = 0
    team2_count = 0
    for team_name in match_tuple:
        if team_name == "Team1" :
            team1_count += 1
        else :
            team2_count += 1
             
    if team1_count == team2_count :
        return "Tie"
         
    elif team1_count > team2_count :
        return "Team1"
     
    else :
        return "Team2"

if __name__ == "__main__" :
     
    print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team"))
