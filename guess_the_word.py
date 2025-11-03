"""
Logan Perry
CIS256 Fall 2024
EX 4_2
Create a word-guessing game where the user guesses a word letter by letter.
You will use Git for version control, pytest for testing, and share your repository on GitHub.
"""
import random

#list of words
words=[
"test",
"blue",
"apple",
"sky",
"game",
"bird",
"water",
"ship",
"food"
]

attempts =3

#Select a random word from a predefined list
def word_picker(input_list):
    picked_word = (random.choice(input_list))
    return picked_word
if __name__ == "__main__":
    word=word_picker(words)

    #for quick testing prints the word
    print(word)

    #ini lists
    correct_list=[]
    wrong_list=[]

    while True:

        #loose condition and break
        if attempts ==0:
            print (f"sorry the word was {word} better luck next time!")
            break

        #prints how many attempts left
        print(f"\nyou have {attempts} attempts to guess the hidden word")

        #prints known letters
        correct_count = 0
        for letter in word:
            if letter in correct_list:
                print (f"{letter}", end='')
                correct_count+=1
            else:
                print("_", end='')
        print("")

        #win condition and break
        if correct_count == len(word):
            print ("YOU WON!")
            break

        #gets input
        guess = input("What letter would you like to guess\n:").lower().strip()

        #if user put more than 1 letter in remind them only 1 letter
        if len(guess) != 1:
            print ("Sorry guess must be 1 letter")

        #if guess was already guessed remind them
        elif guess in correct_list or guess in wrong_list:
            print (f"Sorry you already guessed {guess}")

        #if guess in word...
        elif guess in word:
            correct_list.append(guess)

        #else (guess is not in word)...
        else:
            print(f"{guess} is not in the word")
            wrong_list.append(guess)
            attempts-=1
