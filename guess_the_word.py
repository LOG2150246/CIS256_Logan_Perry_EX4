"""
Logan Perry
CIS256 Fall 2024
EX 4_1
Create a word-guessing game where the user guesses a word letter by letter.
You will use Git for version control, pytest for testing, and share your repository on GitHub.
"""
import random

#list of words
words=[
"test",
"blue",
"apple"
]

attempts =10

#Select a random word from a predefined list
word=(random.choice(words))
#for quick testing prints the word
print(word)

#Prompt the user to guess one letter at a time.


#Reveal letters if the guess is correct; indicate if incorrect.
correct_list=[]
wrong_list=[]

while True:

    #pritns how many attempts left
    print(f"\nyou have {attempts} attempts to guess the hidden word")

    #prints known letters
    for letter in word:
        if letter in correct_list:
            print (f"{letter}", end='')
        else:
            print("_", end='')
    print("")

    #gets input
    guess = input("What letter would you like to guess\n:").lower().strip()

    #if user put more than 1 letter in remind them only 1 letter
    if len(guess) != 1:
        print ("Sorry guess must be 1 letter")

    #if guess was already guessed remind them
    if guess in correct_list or guess in wrong_list:
        print (f"Sorry you already guessed {guess}")

    #if guess in word...
    elif guess in word:
        correct_list.append(guess)

        #print(f"{guess} is in the word")

        #win condition Does NOT work due to 2 letters EX aPPle FIXME
        if len(correct_list)==len(word):
            print("you won")
            break

    #else (guess is not in word)...
    else:
        print(f"{guess} is not in the word")
        wrong_list.append(guess)
        attempts-=1
