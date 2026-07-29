#!/usr/bin/env python3
import json
import os
import datetime
dateData = datetime.datetime.now()
currentYear = dateData.strftime("%Y")

try:
    habitDataFileName=f"habitData-{currentYear}.json"
    #checks if there is a currently existing file, if not, creates data and saves it, else opens file
    if not os.path.exists(habitDataFileName):
        monthsMain = {
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
        with open(habitDataFileName, "w") as file:
            json.dump(monthsMain, file, indent=4)
    else:
        with open(habitDataFileName, "r") as file:
            monthsMain = json.load(file)
    def printSummary(counts):
                activities = list(counts.keys())
                print("SUMMARY")
                for i in range(len(activities)):
                    habit = activities[i]
                    print(f"You did {habit}: {counts[habit]} times.")        
    #prints help menu
    def help():
        print("""\nPossible month values: jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec.\n
                COMMANDS\n
                view: used to print a specific month; USAGE: view MONTH\n
                log: used to log a habit on a specific day; USAGE: log habit month day; can substitue month day with "today"\n
                remove: used to remove a habit from a specific day; USAGE: remove habit month day; can substitute month day with "today"\n
                reset: will wipe all calendar data and quit the program; THERE IS NO WAY TO RECOVER LOST DATA; USAGE: reset\n
                sum: will print a summary of the specified period; You can use a month name, or year to summarize the whole year; USAGE: sum period""")
                

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
    def sumHabitsYear(counts, months):
                monthsList = list(months.keys())
                for i in range(len(monthsList)):
                    currentMonth = monthsList[i]
                    for day in range(len(months[currentMonth])):
                        if not months[currentMonth][day]:
                            continue
                        else:
                            for habit in range(len(months[currentMonth][day])):
                                if months[currentMonth][day][habit] not in counts.keys():
                                    counts[months[currentMonth][day][habit]] = 1
                                else:
                                    counts[months[currentMonth][day][habit]] += 1 
                return counts
    #prints the month specified in terminal, or searches for one
    def printMonth(args, months):
        if not args or args[0].upper() not in months: 
            print("specification invalid, please use format: view month or use command \"help\" for more guidance")
            return
        else:
            userMonth = args[0].upper()
        for i in range(len(months[userMonth])):
            day = months[userMonth][i]
            if len(day)==0:
                print(f"[{(i+1)}]", end="")
            else:
                print("[" + "/".join(day) + "]", end="")
            if (i + 1) % 7 == 0:
                print()
            if (i+1) == len(months[userMonth]):
                print()
    def sumHabits(args, months):
        try:
            counts = {}
            sumPeriod = args[0].lower().strip()
            if  sumPeriod == "year":
                counts = sumHabitsYear(counts, months)
                printSummary(counts)
            elif os.path.exists(f"habitData-{sumPeriod}.json"): 
                with open(f"habitData-{sumPeriod}.json", "r") as file:
                    nonYearMonths = json.load(file)
                sumHabitsYear(counts, nonYearMonths)
                printSummary(counts)
            else:
                userMonth = args[0].upper()
                for day in range(len(months[userMonth])):
                    if not months[userMonth][day]:
                        continue
                    else:
                        for habit in range(len(months[userMonth][day])):
                            if months[userMonth][day][habit] not in counts.keys():
                                counts[months[userMonth][day][habit]] = 1
                            else:
                                counts[months[userMonth][day][habit]] += 1   
                printSummary(counts)
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
        failsafe=input("Are you sure? proceeding will wipe all habit related data and give you a blank calendar. type RESET to proceed\n")
        if failsafe.strip() =="RESET":
            with open (habitDataFileName, "w") as file:
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
                with open(habitDataFileName, "w") as file:
                    json.dump(monthsMain, file, indent = 4)
                quit()


    today = datetime.datetime.now()

        
        
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
                sumHabits(userArgs, monthsMain)
            case "remove":
                removeHabit(userArgs, monthsMain)
            case "reset":
                fullReset()
            case "help":
                help()
            case _:
                print("unrecognized command, use help for guidance")
                continue

except KeyboardInterrupt:
    with open(habitDataFileName, "w") as file:
        json.dump(monthsMain, file, indent=4)
    quit()