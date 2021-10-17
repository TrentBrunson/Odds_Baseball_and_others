#Paired Dice Throwing Probability showing outcomes for dices for 24 times Rolls.
#It shows output of Doubles six probability and any other Doubles for throwing paired die.
#Program output shows 10000 rounds  and each round has 24 Rolls of dices random output finding double sixes and double anyother same number for both die 

#%%
from numpy.core.fromnumeric import nonzero


def rolldice(): #This function gets output for  4-c
    import random
    dieOne = 0
    dieTwo = 0
    doubleSix = 0
    totalDoubleSix = 0
    six = 6
    line=""
    # doubles=0
    one = 1
    zero = 0
    listc = []
    lofl = []
    # glist = []
    gline=""

    with open("round.txt", "w") as wfile:
        with open("gamblehouse.txt", "w") as gfile:        
            for i in range(1,10001):
                line=""
                listc = []
                gline=""
                # glist = []
                doubleSix = 0
                gline = str(i) + "," 
                for dice in range(1,25):
                    line=""
                    dieOne = random.randint(1, 6)
                    dieTwo = random.randint(1, 6)
                    line = str(i) + "," + str(dice) + "," + str(dieOne) + "," + str(dieTwo) + "," 
                    if dieOne == dieTwo: # finds both die has same number
                        line = line + str(one) + ","
                    else:
                        line = line + str(zero) + ","

                    if dieOne == six and dieTwo == six: # finds both die has number six
                        line = line + str(one) 
                        doubleSix += 1
                        totalDoubleSix += 1
                    else:
                        line = line + str(zero)
                    listc.append(line)
                    wfile.write(f"{line}\n")
                if doubleSix >= 1:
                    gline = str(i) + "," + "True" + "," + "Gambler" + "," + str(doubleSix)
                else:
                    gline = str(i) + "," + "False" + "," + "House" + "," + str(zero)
                gfile.write(f"{gline}\n")
            lofl.append(listc)            
        gfile.close()
    wfile.close()       

def gamblehouse(): #This function gets output for  4-d
    import random
    dieOne = 0
    dieTwo = 0
    six = 6
    line=""
    # doubles=0
    # one = 1
    # zero = 0
    listc = []
    lofl = []
    nodoubleSix = (35/36) * 24
    
    with open("gamblehouse.txt", "w") as wfile:
        
        for i in range(1,10001):
            line=""
            listc = []
            doubleSix = 0
            totalDoubleSix = 0

            for dice in range(1,25):
                line=""
                doubleSix = 0
                dieOne = random.randint(1, 6)
                dieTwo = random.randint(1, 6)
                line = str(i) + "," 
                            
                if dieOne == six and dieTwo == six:
                    line = line + "True" + ","
                    doubleSix += 1
                    totalDoubleSix += 1
                else:
                    line = line + "False" + ","
                    
                if doubleSix >= 1:
                    line = line + "Gambler"
                    probofDoublesix = 1 - nodoubleSix
                else:
                    line = line + "House"
                    probofDoublesix = 0
                listc.append(line)
                line = line + "," + str(totalDoubleSix)
                wfile.write(f"{line}\n")            
            # probofDoublesix = 1 - nodoubleSix
            lofl.append(listc)    
    

def optionC(cdata):
    print(cdata)
    import csv
    with open("round.csv", "w", newline="\n") as wfile:
        writer = csv.writer(wfile)
        writer.writerow(cdata)
        #wfile.write(cdata)
        #wfile.close()


def main():
    rolldice()
    #gamblehouse()
    #displayone(cdata)()

if __name__ == "__main__":
    main()
# %%
def rolldice(): #This function gets output for  4-c
    import random
    dieOne = 0
    dieTwo = 0
    doubleSix = 0
    totalDoubleSix = 0
    six = 6
    line=""
    # doubles=0
    one = 1
    zero = 0
    listc = []
    lofl = []
    # glist = []
    gline=""

    with open("roll.csv", "w") as wfile:
        with open("gambler.csv", "w") as gfile:        
            for i in range(1,10001):
                line=""
                listc = []
                gline=""
                doubleSix = 0
                gline = str(i) + "," 
                for dice in range(1,25):
                    line=""
                    dieOne = random.randint(1, 6)
                    dieTwo = random.randint(1, 6)
                    line = str(i) + "," + str(dice) + "," + str(dieOne) + "," + str(dieTwo) + "," 
                    if dieOne == dieTwo: # finds both die has same number
                        line = line + str(one) + ","
                    else:
                        line = line + str(zero) + ","

                    if dieOne == six and dieTwo == six: # finds both die has number six
                        line = line + str(one) 
                        doubleSix += 1
                        totalDoubleSix += 1
                    else:
                        line = line + str(zero)
                    listc.append(line)
                    wfile.write(f"{line}\n")
                if doubleSix >= 1:
                    gline = str(i) + "," + "True" + "," + "Gambler" + "," + str(doubleSix)
                else:
                    gline = str(i) + "," + "False" + "," + "House" + "," + str(zero)
                gfile.write(f"{gline}\n")
            lofl.append(listc)            
        gfile.close()
    wfile.close()
    # return lofl     

def analytics():
    import pandas as pd
    gamblerDF = pd.read_csv('gambler.csv')
    rollDF = pd.read_csv('roll.csv', names=(
        'round_num', 'roll_num', 'die1', 'die2', 'doubles', 'double_six'))
    print(rollDF)
    print("Index: ", rollDF.index)
    print("Columns: ", rollDF.columns)
    print("Size: ", rollDF.size)
    print("Shape: ", rollDF.shape)
    print("Values: ", rollDF.values)
    print("Info: ", rollDF.info())
    rollDF.info()
    double6 = rollDF['double_six'].sum()
    doubles = rollDF['doubles'].sum()
    print(
        f"You just ran a set of 24 rolls, 10,000 times for a total of 240,000 rolls.\n"
        f"You rolled doubles {doubles:,} times, or {doubles/240000:.2%} of the time.\n"
        f"You rolled double sixes {double6:,} times, or {double6/240000:.2%} of the time.\n\n"
        f"In 24 rolls, you typically see double sixes about 49% of the time.\n"
        f"In your 10,000 sets of 24 dice rolls you rolled double sixes {double6/10000:.2%} of the time.\n"    
        )
    if (double6/10000) > .49:
        print("Book your flight to Vegas, baby!\n\n")
    elif (double6/10000) > .4:
        print("Your results are in the range of what is expected.\n\n")
    else:
        print("Better luck next time.\n\n")
    rollDF.groupby('die1')['die1'].agg(['mean','median','std']).plot.bar()

    # import seaborn as sns
    # sns.histplot(rollDF['die1'], bins = 6, legend=False)
    # rollDF["die1"].plot()
    rollDF.groupby('die1')['die1'].agg('count').plot.bar()
    rollDF.groupby('die2')['die2'].agg('count').plot.bar()
    return

def main():
    rolldice()
    analytics()

if __name__ == "__main__":
    main()
# %%

# %%
