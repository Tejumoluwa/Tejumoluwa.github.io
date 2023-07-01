from random import randint as random_number
def main():
    player_list = player_detail()
    player_1 = player_list[0]
    player_2 = player_list[1]
    player_1_bet = stake()
    if player_2 == "2":
        player_2_bet = None
    else:
        player_2_bet = stake()
    fate = play_game(player_1, player_2)
    player_fate(fate, player_1_bet, player_2_bet, player_1, player_2)

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
        print(f"Your bet is ${stake_amount}")
    return stake_amount


# play the game: if player's number > the computer's number, player wins. Else he loses
def play_game(player_1, player_2):
    computer = "computer"
    if player_2 == "2":
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
            player_won = player_1
            player_lost = player_2
        else:
            player_won = player_2
            player_lost = player_1
        return ["win", player_won],["lose", player_lost]



# If player wins: he is to be awarded double the price
def player_fate(fate, player_1_bet, player_2_bet, player_1, player_2):
    if not player_2_bet:
        if fate == "win":
            print("Your win and your earnings are $", player_1_bet * 2)
        elif fate == 'lose':
            print(f"You lose ${player_1_bet}")
    else:
        if fate[0][0] == "win":
            if fate[0][1] == player_1:
                print(f"{fate[0][1]} won and your earnings are ${player_1_bet*2}")
            else:
                print(f"{fate[0][1]} won and your earnings are ${player_2_bet*2}")
        else:
            if fate[1][1] == player_1:
                print(f"{fate[0][1]} lost and you lose ${player_1_bet}")
            else:
                print(f"{fate[1][1]} lost and you lose ${player_2_bet}")
# If the user wants to keep playing

# Main code
main()




