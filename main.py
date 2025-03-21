#Alan Armstrong
#Prog 108
#Programming Final: Word Guessing Game
#6/11/23

#import colorama for some color output

import streamlit as st
import wordlists
import colorama
from colorama import Fore
from colorama import init
init(autoreset=True)

#win/loss dictionary to keep score
scoreboard = {
    "wins" : 0,
    "losses": 0
}

#Welcome message
print("*" * 75)
print()
print(Fore.BLUE + "Welcome to the Word Guessing Game!\n".center(75))
print("*" * 75)
print()

#gets random word from fruit list
def get_fruit():
    fruit = wordlists.get_fruits()
    return fruit.upper()

#gets random word from capitals list
def get_capitals():
    capital = wordlists.get_capitals()
    return capital.upper()

def get_movies():
  movie = wordlists.get_movies()
  return movie.upper()

# Add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# Draw the UI
def draw_UI(count_wrong, count_guesses, guessed_letters, displayed_word):
    print("*" * 75)
    print()
    print(f"{Fore.BLUE} Word:", add_spaces(displayed_word),
        "  Guesses:", count_guesses,
        "  Wrong:", count_wrong,
        f"{Fore.RED}  Tried:", add_spaces(guessed_letters),)
#player inputs next letter
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()
        print()    
        # Make sure the user enters only 1 character, tried to allow spaces but couldn't get it to work
        if len(guess) > 1:
            print("Invalid entry. " +
                "Please enter one and only one letter.")
            continue
        # Don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess

# player selects what category of words to guess from and program gets random word from lists based on selection, then guessing game runs
def play_game():
    difficulty = input("You can get 10 wrong guesses before the game is over. What category of words would you like to guess from? \n\nEnter 1 for (fruits) or 2 for (state capitals) 3 for (movies)")
    print()
    if difficulty == "1":
        word = get_fruit()
    if difficulty == "2":
        word = get_capitals()
    if difficulty == "3":
        word = get_movies()
    
    word_length = len(word)
    remaining_letters = word_length
    displayed_word = "_" * word_length

    count_wrong = 0               
    count_guesses = 0
    guessed_letters = ""

    draw_UI(count_wrong, count_guesses, guessed_letters, displayed_word)

    while count_wrong < 10 and remaining_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess
        
        index = word.find(guess, 0)
        if index != -1:
            displayed_word = ""
            remaining_letters = word_length
            for letter in word:
                if letter in guessed_letters:
                    displayed_word += letter
                    remaining_letters -= 1
                else:
                    displayed_word += "_"              
        else:
            count_wrong += 1

        count_guesses += 1

        draw_UI(count_wrong, count_guesses, guessed_letters, displayed_word)
    print()
    print("*" * 75)
    if remaining_letters == 0:
        print()
        print("Congrats! You guessed it in", count_guesses, "guesses.")
        scoreboard["wins"] += 1
        return scoreboard["wins"]
    else:    
        print("Sorry, you lost.")
        print("The word was:", word)
        scoreboard["losses"] += 1
        return scoreboard["losses"]

def main():
    # print(wordlists.fruits) # test to confirm lists loading
    # print(wordlists.capitals)
    while True:
        play_game()
        print()
        again = input("Would you like to play again (y/n)?: ").lower()
        if again != "y":
          print('Thanks for playing, your score is Wins: {wins} losses: {loss}'.format(wins=scoreboard["wins"], loss=scoreboard["losses"]))
          break

if __name__ == "__main__":
    main()
