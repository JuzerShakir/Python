""" Author : Juzer Shakir   ||  Created on 27 Dec 2017     ||   Last modified on 27 Dec 2017 1:20pm
Topic : A program to split players into 3 random teams
Resources: List of Players given in 'players.txt' file and List of teams given in 'team.txt'. Files in this directory."""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

# importing choice function from random module to choose random element of a list
from random import choice
# giving two empty list for assigning names from respective files
players = []
teams = []

# Opening players file to read it
file_p = open("players.txt", 'r')
# reads the file, each line has single name, 'splitlines()' splits each lines, each element of 'players' list will have one line of "players.txt" file
players = file_p.read().splitlines()
# displays all the name of the players
print('Players :', players, '\n')

# Opening team file to read it
file_t = open('teams.txt', 'r')
# reads the file, each line has single name, 'splitlines()' splits each lines, each element of 'teams' list will have one line of "team.txt" file
teams = file_t.read().splitlines()
# displays all the name of the teams
print('Teams :', teams, '\n')

# Since we need 3 teams, we give three variables to store names, these names will be randomly chosen by 'choice' function
# team name being assigned
teamA = choice(teams)
# now we need to remove the name which has already been assigned to 'teamA' so it doesn't get repeatedly used
teams.remove(teamA)
teamB = choice(teams)
teams.remove(teamB)
teamC = choice(teams)
teams.remove(teamC)

# giving 3 empty lists to store 3 team members name
team_mem_A = []
team_mem_B = []
team_mem_C = []

# using loop to assign players to different team until no one is left
while len(players) > 0:
    # a variable to store the players name
    playerA = choice(players)
    # adding that name to the first team
    team_mem_A.append(playerA)
    # this player has been assigned to a team, so removing from list
    players.remove(playerA)

    # checking if there are players in the list left
    if players == []:
        # if not, the loop breaks
        break

    playerB = choice(players)
    team_mem_B.append(playerB)
    players.remove(playerB)

    if players == []:
        break

    playerC = choice(players)
    team_mem_C.append(playerC)
    players.remove(playerC)


# displaying teams with team players
print('Here are your teams : \n')
print(teamA, ':', team_mem_A)
print(teamB, ':', team_mem_B)
print(teamC, ':', team_mem_C)

# closing both files as opened above to read
file_p.close()
file_t.close()

# That's it!!
