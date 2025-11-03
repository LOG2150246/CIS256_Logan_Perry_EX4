"""
Logan Perry
CIS256 Fall 2024
EX 4_3
Writing Tests Using pytest
"""
import pytest
from guess_the_word import word_picker, words
#from guess_the_word import ...

#The selected word comes from the predefined list
def test_predefined_list():
    word = word_picker(words)
    assert word in words

#Guesses are processed correctly (correct vs. incorrect)
def test_guesses_process():
    print("did stuff")


