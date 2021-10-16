"""
Read the “Scores.txt” file
• Calculate descriptive statistics (mean, standard deviation, number of scores, 
low score, and high score) 
"""
#%%
import csv
scoreList = []
file = "data\Scores.txt"
with open (file) as f:
    for line in f:
        line = int(line.strip())
        scoreList.append(line)
scoreList.sort()

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
else:
    median = scoreList[mid+1]

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

with open("data/Scores-and-Letter-Grades.txt", "w", newline='') as file:
    csv.writer(file, delimiter=",").writerows(newList)
    # file.writelines("%s\n" % item for item in newList)
    # for row in newList:
    #     for item in row:
    #         file.writelines(f"{item},")
    #     file.write("\n")

print(
    f"This program reads a list of grades and computes the descriptive statistics\n"
    f"and writes the grades on the curve output to a new file.\n\n"
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
def getFile():
    import csv
    scoreList = []
    file = "data\Scores.txt"
    with open (file) as f:
        for line in f:
            line = int(line.strip())
            scoreList.append(line)
    scoreList.sort()
    return scoreList

def stats(scoreList):
    total, counter = 0, 0
    for score in scoreList:
        counter += 1
        total += score
    mean = total / counter
    top = max(scoreList)
    bottom = min(scoreList)

    scoreSum = 0
    for score in scoreList:
        scoreSum = scoreSum + (score - mean)**2
    stdev = (scoreSum / counter)**(1/2)

    # grade cut offs
    letterA = mean + 1.5 * stdev
    letterB = mean + .5 * stdev
    letterC = mean - .5 * stdev
    letterD = mean - 1.5 * stdev
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
    return gradeDict, newList, top, bottom, counter, mean, stdev, letterA, letterB, letterC, letterD

def displayWrite(gradeDict, newList, top, bottom, counter, mean, stdev, letterA, letterB, letterC, letterD):
    import csv
    with open("data/Scores-and-Letter-Grades.txt", "w", newline='') as file:
        csv.writer(file, delimiter=",").writerows(newList)
    print(
        f"This program reads a list of grades and computes the descriptive statistics\n"
        f"and writes the grades on the curve output to a new file.\n\n"
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
    return

def main():
    scores = getFile()
    gradeDict, gradeList, best, worst, count, avg, stddev, a, b, c, d = stats(scores)
    displayWrite(gradeDict, gradeList, best, worst, count, avg, stddev, a, b, c, d)

if __name__ == "__main__":
    main()
# %%
