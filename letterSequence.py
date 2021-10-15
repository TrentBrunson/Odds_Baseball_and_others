"""
Sequential, Consecutive Letters Checker. Write a program that asks a user to enter a word or phrase. 
Then check the word/phrase to see if it contains three sequential, consecutive letters. 
Example words/phrases include: “defrost”, “no problem”, “student”, “dabchick”, “crab cakes”, “indefensible”, “deficit”, “burst”,    
“hijab”, “inopportune”, “monopoly”,  “xenophobia”, “tempestuous”, “cause and effect”, “Hi John”, “call me a cab, Carol”, etc. 
(5 points) Use a “markdown” cell in your Jupyter Notebook to introduce your solution for this problem 
and describe any difficulties/issues your team encountered while solving the problem
(5 points) Use a main function to control overall program flowc.(5 points) Write a function to get the user input
(15 points) Write a function to determine if the user input contains three sequential, consecutive letters 
(5 points) Report to the user if the word contains three sequential, consecutive letters
(5 points) Include a program header and appropriate comments to document your code
"""
#!/usr/bin/env python3#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Abecedarian
# PURPOSE:    Determine if the letters of a word are in alphabetical order.
# INPUT:      user word
# PROCESS:    treat the input as a list of characters
# OUTPUT:     yes or no, the word is an abecedarian word
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
#%%
# Set environment and initialize variables
import pandas as pd
choice = "Y"
# %%
choice = "Y"

while choice.upper() == "Y":
    print("This program will determine if you have an abecedarian word.")
    try:
        i = 0
        userWord = input("Enter you word:\n")
        for i in range(len(userWord) - 1):
            if userWord[i] > userWord[i + 1]:
                alpha = False
                break
            else: alpha = True
        if alpha == False:
            print(f"Your word '{userWord}' does not have its letters in alphabetical order.")
        else:
            print(f"Your word '{userWord}' has all of its letters in alphabetical order!")
    except ValueError:
        print("Input words with letters only.\n")

    choice = input("Would you like to try again? (Y/N) ")
# %%
