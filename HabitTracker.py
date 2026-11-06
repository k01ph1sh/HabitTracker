#!/usr/bin/env python3
import json
from pathlib import Path
import datetime
dateData = datetime.datetime.now()
currentYear = dateData.strftime("%Y")

dataPath = Path(Path.home()/"Habit-Tracker")

try:
    def genEmptyData(dataType):
        if dataType == "months":
            monthsMain ={
                "JAN": [[] for i in range(31)],
                "FEB": [[] for i in range(28)],
                "MAR": [[] for i in range(31)],
                "APR": [[] for i in range(30)],
                "MAY": [[] for i in range(31)],
                "JUN": [[] for i in range(30)],
                "JUL": [[] for i in range(31)],
                "AUG": [[] for i in range(31)],
                "SEP": [[] for i in range(30)],
                "OCT": [[] for i in range(31)],
                "NOV": [[] for i in range(30)],
                "DEC": [[] for i in range(31)]
            }
            return monthsMain
        if dataType == "score":
            scoreData = {

            }
            return scoreData
    
    def saveData(data, dataType="all"): 
        if dataType == "months":
            with open(habitDataPath, "w") as f:
                json.dump(data, f, indent=4)
            print("saving month data")
        if dataType == "score":
            with open(scoreDataPath, "w") as f:
                json.dump(data, f, indent=4)
            print("saving Score data")
    
    habitDataFileName=f"habitData-{currentYear}.json"

    scoreDataFileName="scoreData.json"
    #checks if there is a currently existing file, if not, creates data and saves it, else opens file
    
    if not dataPath.exists():
        Path.mkdir(dataPath)

    habitDataPath = Path(dataPath / habitDataFileName)
    scoreDataPath = Path(dataPath / scoreDataFileName)

    if not habitDataPath.exists():
        monthsMain = genEmptyData("months")
        saveData(monthsMain, "months")
        print()
    else:
        with open(habitDataPath, "r") as f:
            monthsMain = json.load(f)    

    if not scoreDataPath.exists():
        scoreData = genEmptyData("score")
        saveData(scoreData, "score")
    else:
        with open(scoreDataPath, "r") as f:
            scoreData=json.load(f)
        


    
    def printSummary(counts, score):
                habitList = list(counts.keys())
                print("SUMMARY")
                for habit in habitList:
                    print(f"You did {habit}: {counts[habit]} times.") 
                print(f"Total Score: {score}")       
    
    #prints help menu
    def printHelp():
        print("""\nPossible month values: jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec.\n
                COMMANDS\n
                view: used to print a specific month; USAGE: view MONTH\n
                log: used to log a habit on a specific day; USAGE: log habit month day; can substitue month day with "today"\n
                remove: used to remove a habit from a specific day; USAGE: remove habit month day; can substitute month day with "today" to use the current date\n
                reset: will wipe all calendar data and quit the program; THERE IS NO WAY TO RECOVER LOST DATA; USAGE: reset\n
                sum: will print a summary of the specified period; You can use a month name, 'month' to use the current month, year to summarize current whole year, or enter the 4 digit year to summarize a previous year; USAGE: sum period\n
                score: allows you to perform various functions related to the scoring of habits; USAGE: 'score habit points' to edit the score with a given habit OR 'score view' to print all habits and associated scores.""")
                

    #takes an arguement and logs it on specific day
    def logHabit(args, months):
        try:
            if args[1].lower().strip() != "today":
                months[args[1].upper()][(int(args[2]) - 1)].append(args[0].upper())
            else:
                time = datetime.datetime.now()
                day = int(time.strftime("%d"))
                month = time.strftime("%b").upper()
                months[month][(day-1)].append(args[0].upper())
        except (ValueError, KeyError):
            print("invalid input, use format <log habit month day>")
        except IndexError:
            print("Specifications not found, use format <log habit month day>")

    def sumHabitsYear(counts, months, scoreData):
                periodScore = 0
                for month, days in months.items():
                    for day in days:
                        if not day:
                            continue
                        else:
                            for habit in day:
                                try:
                                    periodScore += int(scoreData[habit])
                                except KeyError:
                                    pass
                                if habit not in counts.keys():
                                    counts[habit] = 1
                                else:
                                    counts[habit] += 1 
                return counts, periodScore
    #prints the month specified in terminal, or searches for one


    def printMonth(args, months):
        if not args or args[0].upper() not in months: 
            print("specification invalid, please use format: view month or use command \"help\" for more guidance")
            return
        else:
            userMonth = args[0].upper()
        for i, day in enumerate(months[userMonth], start=1):
            if len(day)==0:
                print(f"[{i}]", end="")
            else:
                print("[" + "/".join(day) + "]", end="")
            if i % 7 == 0:
                print()
            if (i) == len(months[userMonth]):
                print()
            
    
    def sumHabits(args, months, scoreData):
        try:
            counts = {}
            sumPeriod = args[0].lower().strip()
            if  sumPeriod == "year":
                counts, score = sumHabitsYear(counts, months, scoreData)
                printSummary(counts, score)
            elif Path.exists(dataPath/ f"habitData-{sumPeriod}.json"): 
                with open(dataPath / f"habitData-{sumPeriod}.json", "r") as f:
                    nonYearMonths = json.load(f)
                sumHabitsYear(counts, nonYearMonths)
                printSummary(counts)
            else:
                periodScore = 0                
                if sumPeriod == "month":
                    currentTime = datetime.datetime.now()
                    userMonth = currentTime.strftime("%b").upper()
                else:
                    userMonth = args[0].upper()
                for day in months[userMonth]:
                    if not day:
                        continue
                    else:
                        for habit in day:
                            try:
                                periodScore+=int(scoreData[habit])
                            except KeyError:
                                pass
                            if habit not in counts.keys():
                                counts[habit] = 1
                            else:
                                counts[habit] += 1   
                printSummary(counts, periodScore)

        except KeyError:
            print("Specifications not found, please use format >sum month/year; use command help for more info")

    # removes a habit from the given date arguments
    def removeHabit(args, months):
        try:
            if args[1].lower().strip() != "today":
                userMonth = args[1].upper()
                day = (int(args[2]) - 1)
                habit = args[0].upper()
                months[userMonth][day].remove(habit)
            else:
                time = datetime.datetime.now()
                day = int(time.strftime("%d"))
                month = time.strftime("%b").upper()
                habit = args[0].upper()
                months[month][(day-1)].remove(habit)                
        except ValueError:
            print("Habit not found")
        except (IndexError, KeyError):
            print("Specifications not found, use format <remove habit month day>")


    def fullReset():
        failsafe=input('Are you sure? proceeding will wipe all habit related data and give you a blank calendar. type "RESET" to proceed\n')
        if failsafe.strip() =="RESET":
            monthsMain = genEmptyData("months")
            saveData(monthsMain)
            scoreData=genEmptyData("score")
            saveData("score")
    

    def modifyScoreData(args, score):
        try:
            habit = args[0].upper()
            newScore= args[1]
            score[habit] = newScore
        except IndexError:
            print("specifications not found, use format '>score habit points'")





    while True:
        userInput = input(">").lower().split()
        if not userInput:
            continue

        command= userInput[0]
        userArgs = userInput[1:]
        match command:
            case "view":
                printMonth(userArgs, monthsMain)
            case "log":
                logHabit(userArgs, monthsMain)
            case "sum":
                sumHabits(userArgs, monthsMain, scoreData)git
            case "remove":
                removeHabit(userArgs, monthsMain)
            case "reset":
                fullReset()
            case "help":
                printHelp()
            case "score":
                modifyScoreData(userArgs, scoreData)
            case "save":
                saveData(monthsMain, "months")
                saveData(scoreData, "score")
            case _:
                print("unrecognized command, use help for guidance")
                continue

except KeyboardInterrupt:
    saveData(monthsMain, "months")
    saveData(scoreData, "score")