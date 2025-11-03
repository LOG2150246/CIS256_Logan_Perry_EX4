"""
Logan Perry
CIS256 Fall 2024
EX 4_3
Writing Tests Using pytest
"""
import pytest
from guess_the_word import word_picker, words,process_guess
#from guess_the_word import ...

#The selected word comes from the predefined list
def test_predefined_list():
    word = word_picker(words)
    assert word in words

#Guesses are processed correctly (correct vs. incorrect)
def test_correct_guess():
    attempts,status= process_guess("a","apple",[],[],3)
    assert status == "correct"

def test_incorrect_guess():
    attempts,status= process_guess("b","apple",[],[],3)
    assert status == "incorrect"
