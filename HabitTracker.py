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
            "JUNE": [[] for i in range(30)],
            "JULY": [[] for i in range(31)],
            "AUG": [[] for i in range(31)],
            "SEPT": [[] for i in range(30)],
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
        pass

    #takes an arguement and logs it on specific day
    def logHabit():
        pass
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
    def sumMonth():
        pass
    def removeHabit():
        pass 
    def fullReset():
        failsafe=input("Are you sure? proceeding will wipe all habit related data and give you a blank calendar. type RESET to proceed\n")
        if failsafe =="RESET":
            with open ("habitData.json", "w") as file:
                monthsMain ={
                "JAN": [[] for i in range(31)],
                "FEB": [[] for i in range(28)],
                "MAR": [[] for i in range(31)],
                "APR": [[] for i in range(30)],
                "MAY": [[] for i in range(31)],
                "JUNE": [[] for i in range(30)],
                "JULY": [[] for i in range(31)],
                "AUG": [[] for i in range(31)],
                "SEPT": [[] for i in range(30)],
                "OCT": [[] for i in range(31)],
                "NOV": [[] for i in range(30)],
                "DEC": [[] for i in range(31)]
                }
                json.dump(monthsMain, file, indent = 4)


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
        userInput = input(">").split()
        if not userInput:
            continue

        command= userInput[0]
        userArgs = userInput[1:]
        match command:
            case "view":
                printMonth(userArgs, monthsMain)
            case "log":
                logHabit()
            case "summary":
                sumMonth()
            case "remove":
                removeHabit()
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

    
