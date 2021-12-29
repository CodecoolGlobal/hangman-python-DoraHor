from hangman import list_of_letters


# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
# difficulty = "1" # sample data, normally the user should choose the difficulty

import random

import sys

level = ("1", "2", "3")
lives = 0
act_level = 0
difficulty1 = []
difficulty2 = []
difficulty3 = []
list_of_letters = []
lenght = []



def ask_level():
    while True:
        level_in = input("Select the desired level! (1,2,3) ")
        if valid_level(level_in):
            act_level = int(level_in)
            return level_in
        elif level_in.lower() == str("quit"):
            print("Goodbye")
            sys.exit(0)    
        else:
            print("Please choose 1,2 or 3! ")
            return level_in
    


def valid_level(level_in):
    if level_in in level:
        return True
    else:
        return False

def number_of_lives(level_in):
    lives = int(level_in) + 5
    return lives
   

def words_preproc():
    f = open(r"C:\Users\dorah\OneDrive\Dokumentumok\hangman-python-DoraHor\countries-and-capitals.txt", "r")
    file_content = f.readlines()
    for x in file_content:
        a = x.split("|")
        b = len(a[0])
        if b < 11:
            difficulty1.append(a[0])
        elif 21 > b > 10:
            difficulty2.append(a[0])
        elif b > 20:
            difficulty3.append(a[0])
        c = len(a[1])
        if c < 11:
            difficulty1.append(a[1])
        elif 21 > c > 10:
            difficulty2.append(a[1])
        elif c < 20:
            difficulty3.append(a[1])
    

def random_word(act_level):
    word_to_guess = random.choice(difficulty1)
    return trim_the_word(word_to_guess)

def trim_the_word(input):
    return list(input.strip())




def hangman_core(word_to_guess, already_tried_letters,lives,level_in):
    guessed = False
    already_tried_letters = set()
    word_to_guess_upper = []
    for e in word_to_guess:
        word_to_guess_upper.append(e.upper())
    # print(word_to_guess)
    while not guessed and lives > 0:
        letters = input("Please give me a letter! ").upper()
        if letters == "QUIT":
            print("Goodbye")
            sys.exit(0) 
        if letters in already_tried_letters:
            print("You already guessed the letter", letters)
        elif letters in word_to_guess_upper:
            print("Good job,", letters, " is in the word!")
            already_tried_letters.add(letters)
        else:
            print(letters, " is not in the word. ")
            lives -= 1 
            already_tried_letters.add(letters)
        # show_the_word(word_to_guess,already_tried_letters)
        word_completion = show_the_word(word_to_guess,already_tried_letters)
        print('Lives: ', lives)
        if lives == 0:
            print("MUCH TO LEARN YOU STILL HAVE, MY YOUNG PADAWAN!")
            merged_word_to_guess = [''.join(word_to_guess)]
            print("THE WORD WAS: ", str(merged_word_to_guess))
        hangman(lives,level_in)
        if "_" not in word_completion:
            print(" Boom! Nailed it! Congrats! :) ")
            break
    # print(already_tried_letters)      
    return already_tried_letters, lives

def show_the_word(word_to_guess, already_tried_letters):
    l = []
    for x in word_to_guess:
        if x.upper() in already_tried_letters:
            l.append(x)
        else:
            l.append('_')
    print(''.join(l))
    return l

# print the hangman

def hangman(lives,level_in): 

    if level_in == "1" and lives == 6:
        print("""""")

    if level_in == "1" and lives == 5 or level_in =="2" and lives == 6 or level_in == "3" and lives == 7:
        print("""
________ """)


    if level_in == "1" and lives == 4 or level_in =="2" and lives == 5 or level_in == "3" and lives == 6:
        print("""
                
|     
|      
|     
|     
|
|________""") 


    if level_in == "1" and lives == 3 or level_in =="2" and lives == 4 or level_in == "3" and lives == 5:
        print("""
--------                
|     
|     
|     
|     
|
|________""")

    if level_in == "1" and lives == 2 or level_in =="2" and lives == 3 or level_in == "3" and lives == 4:
        print("""
--------                
|      0
|     
|     
|     
|
|________""")

    if level_in == "1" and lives == 1:
        print("""
--------                
|      0
|     /|\ 
|      |
|     
|
|________""")

    if level_in == "2" and lives == 2:
        print("""
--------                
|      0
|      |
|      |
|     
|
|________""")

    if level_in == "2" and lives == 1:
        print("""
--------                
|      0
|     /|\
|      |
|     
|
|________""")

    if level_in == "3" and lives == 3:
        print("""
--------                
|      0
|      |
|      |
|     
|
|________""")

    if level_in == "3" and lives == 2:
        print("""
--------                
|      0
|     /|
|      |
|     
|
|________""")

    if level_in == "3" and lives == 1:
        print("""
--------                
|      0
|     /|\
|      |
|     
|
|________""")

    if lives == 0:
        print("""
--------                
|      0
|     /|\ 
|      |
|     / \
|
|
|________""")

    return lives, level_in 


def main():
    username = input("What is your username? ")
    print("Welcome ", username, " Let's play hangman!:) ")
    if username.lower() == str("quit"):
            print("Goodbye")
            sys.exit(0)  
    level_in = ask_level()
    lives = number_of_lives(level_in)
    print('Lives:', (lives))
    words_preproc()
    word_to_guess = random_word(level_in)
    already_tried_letters = set()
    already_tried_letters, lives = hangman_core(word_to_guess, already_tried_letters, lives, level_in)
    already_tried_letters = show_the_word(word_to_guess, already_tried_letters)
    # lives, level_in = hangman(lives,level_in)
    


if __name__ == '__main__':
    main()



    
# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
# word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
# lives = 5 # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
# already_tried_letters = [] # this list will contain all the tried letters


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.



# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4


