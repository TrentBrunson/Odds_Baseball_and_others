#Paired Dice Throwing Probability showing outcomes for dices for 24 times Rolls.
#It shows output of Doubles six probability and any other Doubles for throwing paired die.
#Program output shows 10000 rounds  and each round has 24 Rolls of dices random output finding double sixes and double anyother same number for both die 

#%%

def rolldice(): #This function gets output for  4-c
    import random
    dieOne = 0
    dieTwo = 0
    doubleSix = 0
    totalDoubleSix = 0
    six = 6
    line=""
    doubles=0
    one = 1
    zero = 0
    listc = []
    lofl = []
    #import csv
    #with open("round.csv", "w", newline="\n") as file:
        #writer = csv.writer(file)
    with open("round.txt", "w") as wfile:
                
        for i in range(1,10001):
            line=""
            listc = []
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
            
                #print(line)
                listc.append(line)
                wfile.write(f"{line}\n")
                #writer.writerow(line)
            
            lofl.append(listc)    
        #print(lofl)
        print(doubleSix)
        return lofl        

def gamblehouse(): #This function gets output for  4-d
    import random
    dieOne = 0
    dieTwo = 0
    six = 6
    line=""
    doubles=0
    one = 1
    zero = 0
    listc = []
    lofl = []
    nodoubleSix = (35/36) ** 24
    
    with open("gamblehouse.csv", "w") as wfile:
        
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
                    print(f"Gambler is the winner! {totalDoubleSix}")
                else:
                    line = line + "House"
                    probofDoublesix = 0
                    
                #print(line)
                listc.append(line)
                line = line + "," + str(totalDoubleSix)
                wfile.write(f"{line}\n")
                #writer.writerow(line)
            
            probofDoublesix = 1 - nodoubleSix
            lofl.append(listc)    
    

def optionC(cdata):
    print(cdata)
    import csv
    with open("round.csv", "w", newline="\n") as wfile:
        writer = csv.writer(wfile)
        writer.writerow(cdata)
        #wfile.write(cdata)
        #wfile.close()

def displayone(cdata):
    with open("round.txt", "w") as wfile:
        for row in cdata:
            wfile.write(f"{row}\n")
    wfile.close()   
      

def main():
    cdata = rolldice()
    gamblehouse()
    #displayone(cdata)()
    



if __name__ == "__main__":
    main()

# %%
