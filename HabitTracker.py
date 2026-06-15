#!/usr/bin/env python3
import json
import os
import datetime



try:
    if os.path.exists("habitData.json"):
        with open("habitData.json", "r") as file:
            months=json.load(file)
    else:
        months= {
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


    def logHabit():
        pass
    def printMonth():
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
    commands= {
        "log": logHabit,
        "view": printMonth,
        "summary": sumMonth,
        "remove" : removeHabit
}

    today = datetime.datetime.now()
    def modCalender (habit, day, months, month):
        months[month][(int(day)-1)].append(habit)
    def getModSpecs(month, months):
        while True:

            while True:
                modDay=input("What day would you like to log X habit? (enter just the num)\n")
                try:
                    int(modDay)
                    break
                except ValueError:
                    print("Please enter a number")
            if int(modDay)>len(months[month]):
                print(f"please enter a valid day, {month} is {len(months[month])} days long.")
            else:
                break
        modHabit=input(f"what would you like to log on {modDay}, {month}?\n")
        return modHabit, modDay

    while True:
        userMonth = input("What month would you like to view?\n")
        userMonth = userMonth.upper()
        if userMonth not in months.keys():
            print("month not found")
        else:
            printMonth()
            edit = input("Would You like to log anything? (Y/N) \n")
            if edit.upper() == "Y":
                modHabit, modDay = getModSpecs(userMonth, months)
                modCalender(modHabit, modDay, months,userMonth)
                printMonth()
                with open("habitData.json", "w") as file:
                    json.dump(months, file, indent=4)
except KeyboardInterrupt:
    with open("habitData.json", "w") as file:
        json.dump(months, file, indent=4)
    quit

    
