import random
import sys
def main():
    HiddenWord = random.choice(["cabin", "eager", "habit", "labor", "sober"])
    lives = 6
    rules()
    for _ in range(lives):
        print(f"You have {lives} lives remaining")
        lives -= 1
        UserGuess =  GetInput()
        FB =  FeedBack(UserGuess, HiddenWord)
    print("Oops, looks like you didn't get it")


# Rules of the game
def rules():
     print("""Welcome to Wordle, a game you guess a 5 letter word. There are clues to help you along the way.
		        If you see '%', the letter in the word you guessed is correct and in the right position
		        If you see '+', the letter is in the word but in the wrong position.
		        If you see 'x', the letter is not in the word.
		        Enjoy your game!!""")


# GetInput Definition
def  GetInput():
    while True:
        UserInput = input("Give me a five letter word ").lower()
        if len(UserInput) == 5:
            return UserInput
        else:
            print("The word must be a five letter word")
        


# FeedBack Definition
def FeedBack(Ug, word):
    word2 = ""
    if Ug == word:
        sys.exit("You are correct")
    else:
        indices = 0
        while indices < len(word):
            if Ug[indices] == word[indices]:
                word2 += "%"
            elif Ug[indices] in word:
                word2 += "+"
            else:
                word2 += "x"
            indices += 1
        print(word2)

    


if __name__ == "__main__":
    main()