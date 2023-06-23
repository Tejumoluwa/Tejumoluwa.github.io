from random import randint as random_number


# Create the player's as player_1, player_2, computer
def player_detail():
    player_1 = input("What is your name: ")
    print("Welcome to the Hero's betting platform where only smart players take the loot.")
    player_2 = input("Type 1 if you want to play with friend or 2 if you want to play with computer: ")
    if player_2 == '1':
        player_2 = input("What is your friend's name: ")
    return player_1, player_2


# create a stake
def stake():
    stake = [5, 7, 10]
    # place bet
    print("Place your bet")
    stake_amount = int(input("Type 5 for $5, 7 for $7 and 10 for $10: "))
    while stake_amount not in stake:
        print("Try again")
        stake_amount = int(input("Type 5 for $5, 7 for $7 and 10 for $10: "))
    if stake_amount in stake:
        print(f"Your bet is {stake_amount}")
    return stake_amount


# play the game: if player's number > the computer's number, player wins. Else he loses
def play_game(player_1, player_2):
    computer = "computer"
    if player_2 != 2:
        player_1_dice = input("Type y to roll your dice: ").lower()
        if player_1_dice == 'y':
            player_1_num = random_number(1, 6)
            print(f"{player_1} played {player_1_num}")
            computer_num = random_number(1,6)
            print(f"The computer played {computer_num}")
            if player_1_num >= computer_num:
                return "win"
            else:
                return "lose"
    else:
        player_1_dice = input("Type y to roll your dice: ").lower()
        if player_1_dice == 'y':
            player_1_num = random_number(1, 6)
            print(f"{player_1} played {player_1_num}")
        player_2_dice = input("Type y to roll your dice: ").lower()
        if player_2_dice == 'y':
            player_2_num = random_number(1, 6)
            print(f"{player_2} played {player_2_num}")
        if player_1_num > player_2_num :
            return "win", player_1
        elif player_2_num > player_1_num:
            return "lose", player_2


# If player wins: he is to be awarded double the price
def player_fate(fate, bet):
    if fate[0] == "win" or fate == "win":
        print("Your win and your earnings are $", bet*2)
    elif fate[0] == "lose" or fate == 'lose':
        print(f"You lose ${bet}")
# If the user wants to keep playing

# Main code
player_list = player_detail()
player_1 = player_list[0]
player_2 = player_list[1]
bet = stake()
fate = play_game(player_1, player_2)
player_fate(fate, bet)




