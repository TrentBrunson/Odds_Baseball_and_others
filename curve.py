"""
Read the “Scores.txt” file
• Calculate descriptive statistics (mean, standard deviation, number of scores, low score,
and high score) – NOTE: While there are several libraries available with functions to 
Last modified: September 28, 2021 Page 3 of 6
calculate descriptive statistics, I am requiring you to write your own code to do these
calculations (see Figure 1 for standard deviation formula).
• Display the descriptive statistics in a nicely formatted table (see Figure 2) – (NOTE: For
the formatted table, you should round the average and standard deviation values for
DISPLAY PURPOSES ONLY.)
• Use the grade curve table to determine the letter grade for each numeric score (NOTE:
Use the unrounded average and standard deviation values to calculate the cutoff
points. Round the cutoff points to 1 place after the decimal when determining letter
grades.)
• Create a new file named “Scores-and-Letter-Grades.txt” that contains the score and
letter grade on the same line (see sample first lines of new file in Figure 3)
• Count the total number of scores for each letter grade (i.e., number of As, Bs, Cs, etc.) –
HINT: A dictionary is an efficient tool for accumulating counts.
• Display a curved grade cut-off-point table (see Figure 2)
• Display a grade distribution table (see Figure 2)
"""
#%%
scoreList = []
file = "data\Scores.txt"
with open (file) as f:
    for line in f:
        line = int(line.strip())
        scoreList.append(line)
scoreList.sort()
# %%
total, counter = 0, 0
for score in scoreList:
    counter += 1
    total += score
mean = total / counter
top = max(scoreList)
bottom = min(scoreList)

mid = int(round(len(scoreList)/2, 0))

if counter % 2 == 0:
    median = (scoreList[mid] + scoreList[mid+1])/2
    print(scoreList[mid], mid, scoreList[mid+1])
else:
    median = scoreList[mid+1]

print(counter,total,mean,median,top, bottom)

scoreSum = 0
for score in scoreList:
    scoreSum = scoreSum + (score - mean)**2
stdev = (scoreSum / counter)**(1/2)

# grade cut offs
letterA = mean + 1.5 * stdev
letterB = mean + .5 * stdev
letterC = mean - .5 * stdev
letterD = mean - 1.5 * stdev
letterF = mean - 1.5 * stdev

countA = 0
countB = 0
countC = 0
countD = 0
countF = 0
gradeDict = {'A':0,'B':0,'C':0,'D':0,'F':0}
newList = []
for score in scoreList:
    if round(score,1) >= letterA:
        countA += 1
        newList.append([score,'A'])
    elif round(score,1) >= letterB:
        countB += 1
        newList.append([score,'B'])
    elif round(score,1) >= letterC:
        countC += 1
        newList.append([score,'C'])
    elif round(score,1) >= letterD:
        countD += 1
        newList.append([score,'D'])
    else:
        countF += 1
        newList.append([score,'F'])


gradeDict.update({'A':countA})
gradeDict.update({'B':countB})
gradeDict.update({'C':countC})
gradeDict.update({'D':countD})
gradeDict.update({'F':countF})
print(gradeDict)
with open("data/Scores-and-Letter-Grades.txt", "w") as file:
    for row in newList:
        # file.writelines("%s\n" % item for item in newList)
        file.writelines(row)
#%%


print(
    f"Count:\t\t\t{counter}\n"
    f"Average:\t\t{round(mean,2)}\n"
    f"Standard deviation:\t{round(stdev,2)}\n"
    f"Maximum:\t\t{top}\n"
    f"Minimum:\t\t{bottom}\n\n"
    f"Curved Grade - Cut Off Points (to 1 decimal place)\n"
    f"A:   {round(letterA,1)}\n"
    f"B:   {round(letterB,1)}\n"
    f"C:   {round(letterC,1)}\n"
    f"D:   {round(letterD,1)}\n\n"
    f"GRADE DISTRIBUTION AFTER CURVING GRADES USING CUT \nOFF POINTS FROM ABOVE\n"
    f"A:  {gradeDict['A']}\tB:  {gradeDict['B']}\tC:  {gradeDict['C']}\tD:  {gradeDict['D']}\tF:  {gradeDict['F']}\t"
)
# %%

# %%
mid = len(scoreList)/2
mid
# %%
4**2

# %%
4**(1/2)
# %%
13**1/2
# %%
