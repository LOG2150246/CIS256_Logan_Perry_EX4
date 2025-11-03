"""
Logan Perry
CIS256 Fall 2024
EX 4_1
Create a word-guessing game where the user guesses a word letter by letter.
You will use Git for version control, pytest for testing, and share your repository on GitHub.
"""
import random
from random import randint

#list of words
words=[
"test",
"blue",
"apple"
]

#Select a random word from a predefined list
word=(random.choice(words))
print(word)
#Prompt the user to guess one letter at a time.

#Reveal letters if the guess is correct; indicate if incorrect.

#Continue until the user guesses the word or runs out of attempts.

#Display a congratulatory message when the word is guessed.