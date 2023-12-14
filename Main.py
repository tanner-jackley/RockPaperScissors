from random import randint

# return random pick of 'ROCK' 'PAPER' or 'SCISSORS'
def get_computer_choice():
    return RPC[randint(0, 2)]

# return valid user input 'ROCK' 'PAPER' or 'SCISSORS'
# also accepts 'R' 'P' or 'S' respectively
# handles case sensitivity and incorrect input
def get_player_choice():
    player_choice = ""
    while player_choice not in RPC and player_choice not in RPC_short:
        player_choice = input("Select 'rock', 'paper' or 'scissors' (r, p, s): ").upper()
    if player_choice in RPC_short: player_choice = RPC[RPC_short.index(player_choice)]
    return player_choice

# param pc: player choice, cc: computer choice
# return 'TIE' 'PLAYER' or 'COMPUTER' based on params
def decide_round_winner(pc, cc):
    if pc == cc: return "TIE"
    elif pc == "ROCK" and cc == "SCISSORS" or pc == "PAPER" and cc == "ROCK" or pc == "SCISSORS" and cc == "PAPER":
        return "PLAYER"
    else:
        return "COMPUTER"

# param result: result of decided_winner
# print result based on param
def print_round_result(result):
    if result == "TIE":
        print("      It's a tie!")
    elif result == "PLAYER":
        print("      Player Wins")
    else:
        print("     Computer Wins")

# return high score from 'scoreboard.txt'
def get_high_score():
    f = open("highscore.txt", "r")
    current_high_score = f.read()
    f.close()

    return int(current_high_score)

# param score: current win streak
# sets 'scoreboard.txt' if param > high score
def set_highscore(score):
    if score > get_high_score():
        f = open("highscore.txt", "w")
        f.write(str(score))
        f.close()



RPC = ["ROCK", "PAPER", "SCISSORS"]
RPC_short = ["R", "P", "S"]
game_running = True
win_streak = 0

# game loop 
while game_running:
    computer_wins = 0
    player_wins = 0
    round = 0
    win_target_number = 3

    print("               ROCK PAPER SCISSORS")
    print("=================== Best of 5 ===================\n")

    # if player has win streak, show streak and high score
    if win_streak > 0:
        print(f"Win streak: {win_streak}")
        set_highscore(win_streak)
        print(f"Higheset win streak: {get_high_score()}\n")
    
    # generates new round until player or computer hits target number
    while computer_wins < win_target_number and player_wins < win_target_number:
        round += 1
        print(f"-------------------- Round {round} --------------------")

        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"\nComputer picked: {computer_choice} \n")

        result = decide_round_winner(player_choice, computer_choice)
        print_round_result(result)
        
        if result == "PLAYER": player_wins += 1
        elif result == "COMPUTER": computer_wins += 1

        print(f"Player | {player_wins} | {computer_wins} | Computer")
        print("-------------------------------------------------\n")

    # print winner of game
    # if player wins, increase win_streak
    # (last result from above while loop determines overall winner)
    if result == "PLAYER": 
        win_streak += 1
        print("PLAYER WINS!\n")
    elif result == "COMPUTER": 
        win_streak = 0
        print("COMPUTER WINS\n")

    print("=================================================\n")

    # ask user to continue game, only stops loop if user inputs 'N'
    if input("Want to play again? ('Y' or 'N'): ").upper() == "N":
        game_running = False

    print("\n\n")