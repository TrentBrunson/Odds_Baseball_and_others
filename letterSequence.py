#!/usr/bin/env python3#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Abecedarian
# PURPOSE:    Determine if the word or phrase has three sequential letters.
# INPUT:      user word/phrase
# PROCESS:    treat the input as a list of characters and cycle through the list
# OUTPUT:     yes or no, the word has three sequential characters
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
#%%
# Set environment and initialize variables
import pandas as pd
choice = "Y"
# %%
choice = "Y"

while choice.upper() == "Y":
    # header telling user the purpose of the program and taking input
    print("This program will determine if your phrase has three letters in sequential order.")
    entry = (input("Enter you word:\n"))
    # check = entry.isalpha()
    if (entry.isalpha() == True):  # error handling for non-strings
        # remove spaces for processing and assign to new variable
        userWord = entry.lower().replace(" ","")  
        if len(userWord)<3:  # make sure the word is long enough for proecssing
            print("You need to enter a word or phrase longer than 3 characters.")
        else:
            # reset counters and boolean variable
            sequential = False
            i,j = 0,1 # initialize counters for loops
            for i in range(len(userWord)-1): # set length of loop to user input
                # print(i, userWord, len(userWord))
                # check if letters are sequential as looping through letters in the input
                if (ord(userWord[i]) + 1) == (ord(userWord[i+1])):
                    # print(ord(userWord[i]), (ord(userWord[i+1])))
                    j += 1 # increment inner counter only when two letters are sequential
                    # print(sequential, i, j)
                    if j == 3:
                        # if found three sequential letters in a row, 
                        # return positive result and end processing
                        sequential = True
                        print(f"{entry} has three sequential letters.", sequential)
                        break
                else:
                    j = 1 # reset counter to start with first letter
                print(f"{entry} does not have three sequential letters.", sequential)
    else:
        print("Input words with letters only.\n")

    choice = input("Would you like to try again? (Y/N) ")
# %%
def userInput():
    # header telling user the purpose of the program and taking input
    print("This program will determine if your phrase has three letters in sequential order.")
    entry = (input("Enter you word or phrase:\n"))
    # remove numbers, spaces and special characters; convert to all lowercase for evaluation
    # use .join to return string instead of iterable object from filter
    userWord = ''.join(filter(str.isalpha, entry)).lower()
    # userWord = entry.lower().replace(" ","")  
    if len(userWord)<3:  # make sure the word is long enough for proecssing
        print("You need to enter a word or phrase longer with 3 or more characters.\n")
    # elif (userWord.isalpha() == False):  # error handling for non-strings
    #     print("Input words with letters only.\n")
        entry = False
    
    else: pass
    return entry, userWord

def result(userWord):
    sequential = False
    i,j = 0,1 # initialize counters for loops
    for i in range(len(userWord)-1): # set length of loop to user input
        # print(i, userWord, len(userWord))
        # check if letters are sequential as looping through letters of the input
        if (ord(userWord[i]) + 1) == (ord(userWord[i+1])):
            # print(ord(userWord[i]), (ord(userWord[i+1])))
            j += 1 # increment inner counter only when two letters are sequential
            # print(sequential, i, j)
            if j == 3:
                # if found three sequential letters in a row, 
                # return positive result and end processing
                sequential = True
                # print(f"{entry} has three sequential letters.", sequential)
                break
        else:
            j = 1 # reset counter to start with first letter 
    return sequential

def output(expression, entry):
    if expression == True:
        print(f"{entry} has three sequential letters.\n")
    else: 
        print(f"{entry} does not have three sequential letters.\n")
    return

def main():
    choice = "Y"
    while choice.upper() == "Y":
        entry, compressedEntry = userInput()
        if entry == False:
            continue
        valid = result(compressedEntry)
        output(valid,entry)
        choice = input("Would you like to try again? (Y/N) ")
    return

if __name__ == "__main__":
    main()
# %%
