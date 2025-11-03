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
    print(f"{attempts} attempts left")
    guess = input("What letter would you like to guess\n:")

    if guess in word:
        correct_list=[].append(guess)
        print(f"{guess} is in word")

    else:
        print(f"{guess} is not in the word")
        wrong_list = [].append(guess)
    attempts-=1

#Continue until the user guesses the word or runs out of attempts.

#Display a congratulatory message when the word is guessed.