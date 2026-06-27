#!/usr/bin/env python3
import json
import os
import datetime



try:
    #checks if there is a currently existing file, if not, creates data and saves it, else opens file
    if not os.path.exists("habitData.json"):
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
        with open("habitData.json", "w") as file:
            json.dump(monthsMain, file, indent=4)
    else:
        with open("habitData.json", "r") as file:
            monthsMain = json.load(file)

    #prints help menu
    def help():
        print("""\nPossible month values: jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec.\nCOMMANDS\nview: used to print a specific month; USAGE: view MONTH\nlog: used to log a habit on a specific day; USAGE: log habit month day; can substitue month day with "today"\nremove: used to remove a habit from a specific day; USAGE: remove habit month day; can substitute month day with "today"\nreset: will wipe all calendar data and quit the program; THERE IS NO WAY TO RECOVER LOST DATA; USAGE: reset""")

    #takes an arguement and logs it on specific day
    def logHabit(args, months):
        try:
            if args[1].lower().strip() != "today":
                months[args[1].upper()][(int(args[2]) - 1)].append(args[0])
            else:
                time = datetime.datetime.now()
                day = int(time.strftime("%d"))
                month = time.strftime("%b").upper()
                months[month][(day-1)].append(args[0])
        except (ValueError, KeyError):
            print("invalid input, use format <log habit month day>")
        except IndexError:
            print("Specifications not found, use format <log habit month day>")
                
    #prints the month specified in terminal, or searches for one
    def printMonth(args, months):
        if not args or args[0].upper() not in months: 
            userMonth= input("specification not found, please pick a month\n>").upper()
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
    def sumMonth(args, months):
            counts = {}
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
            print(counts)
    #removes a habit from the given date arguments
    def removeHabit(args, months):
        try:
            if args[1].lower().strip() != "today":
                months[args[1].upper()][(int(args[2])-1)].remove(args[0])
            else:
                time = datetime.datetime.now()
                day = int(time.strftime("%d"))
                month = time.strftime("%b").upper()
                months[month][(day-1)].remove(args[0])                
        except ValueError:
            print("Habit not found")
        except (IndexError, KeyError):
            print("Specifications not found, use format <remove habit month day>")
    def fullReset():
        failsafe=input("Are you sure? proceeding will wipe all habit related data and give you a blank calendar. type RESET to proceed\n")
        if failsafe.strip() =="RESET":
            with open ("habitData.json", "w") as file:
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
                with open("habitData.json", "w") as file:
                    json.dump(monthsMain, file, indent = 4)
                quit()


    commands= {
        "log": logHabit,
        "view": printMonth,
        "summary": sumMonth,
        "remove" : removeHabit,
        "reset" : fullReset
}

    today = datetime.datetime.now()
    def modCalender (habit, day, months, month):
        months[month][(int(day)-1)].append(habit)
    def getModSpecs(month, months):
        pass
        
        
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
            case "summary":
                sumMonth(userArgs, monthsMain)
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
    with open("habitData.json", "w") as file:
        json.dump(monthsMain, file, indent=4)
    quit()