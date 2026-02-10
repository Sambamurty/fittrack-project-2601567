player_name = input("Enter player's name: ")
no_of_games = input("Enter number of games played: ")

no_of_games = int(no_of_games)
total_score = int(input("Enter total score: "))
average_score = total_score / no_of_games

print(f"Player: {player_name}\nGames Played: {no_of_games}\nTotal Score: {total_score}\nAverage Score: {average_score}")