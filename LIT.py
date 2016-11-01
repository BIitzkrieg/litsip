#!/usr/bin/env python3

##Andrew Danis
##LIT Protoype
##10-26-16

##################Imports##################
import sys
import os
import subprocess


##################Functions##################
##print sys info
def sysInfo():
    os.system("lsb_release -a;  df -h")
    repeatDiag()
    
    
##
def getTasks():
    print('hi')
    
    
##
def getServices():
    print('hi')

##Get About
def getAbout():
    print('%-200s'%"LIT is a Student Innovation Project by Andrew Danis and Zach Evans.\nInspired by the common tasks required at the Collegiate Cyber Defense Competition, LIT is designed to provide the user with an easy to use, navigable script that will help them easily diagnose and harden their Linux based system.\nLIT is for both the security and non security minded people alike, and we hope that the user will be able to learn something along the way.")    
    mainFunction()
##
def getAccounts():
    print('hi')

def getConnections():
    print('hi')
 


## Bool return for a user inputed integer string
def validInteger(string):
    index = -1
    for char in string:
        index += 1
        if (index == 0 and char[index] == '-' and len(string) > 1):
            continue
        elif not (char in "0123456789"):
            return False
    return True
##Only allows the user to test for functions 1-7
def validInput(string):
    if (string == "1" or string == "2" or string == "3" or string == "4" or string == "5" or string == "6" or string == "7"): 
        return True
    else:
        return False
##function to repeat mainFunction
def repeat():
    while True:
        response = input("Would you like to return to the main menu? (y/n) ").lower()
        if response in ['n', 'no']:
            print("Exiting...")
            sys.exit()
        elif response in ['y', 'yes']:
            print("Going to Menu")
            mainFunction()
        else:
            print("Invalid input.. ")
            
##function to repeat diagMenu
def repeatDiag():
    daddy = False
    while True:
        response = input("Would you like to return to the Diagnostic menu? (y/n) ").lower()
        if response in ['n', 'no']:
            print("Exiting...")
            sys.exit()
        elif response in ['y', 'yes']:
            print("Going to Menu")
            diagMenu()
            return daddy 
        else:
            print("Invalid input.. ")

##
def symbolInfo():
        print('hi')
        
            
#############Menus#########################    
def diagMenu():
    print()
    print("########Diagnostic Menu########")
    print()
    print("[ 1 ]  System Info")
    print("[ 2 ]  Scheduled Tasks")
    print("[ 3 ]  Enabled/Running Services")
    print("[ 4 ]  Display User Accounts")
    print("[ 5 ]  Display Active Connections")
    print("[ 6 ]  Return to Main Menu")
    print("[ 7 ]  Exit")
    print()
    userInput = input("Pick a function to run: ")
    while not validInput(userInput):
        userInput = input("Please enter a valid input. [ 1-7 ] ")
    userInput = int(userInput)
    ##Call Sys Info
    if userInput == 1:
        print()
        print("#####System Info######")
        sysInfo()
        print()
    ##Call Scheduled Tasks
    if userInput == 2:
        print()
        print("####Scheduled Tasks######")
        getTasks()
    ##Call Services   
    if userInput == 3:
        print()
        print("######Enabled/Running Services######")
        getServices()
    ##Call Accounts  
    if userInput == 4:
        print()
        print("######User Accounts######")
        getAccounts()
    ##Call Active Connections  
    if userInput == 5:
        print()
        print("######Active Connections######")
        getConnections()
    ##Call Menu   
    if userInput == 6:
        print()
        print("######We're Going Back Marty######")
        mainFunction()

    ##Exit Program
    if userInput == 7:
          return False

           

##################Print Statements/Input/Main##################
##Main Menu
def mainFunction():
    print()
    print("########Main Menu########")
    print()
    print("[ 1 ]  Diagnostic Menu")
    print("[ 2 ]  Hardening Menu")
    print("[ 3 ]  About")
    print("[ 4 ]  Exit")
    print()
    userInput = input("Pick a function to run: ")
    while not validInput(userInput):
        userInput = input("Please enter a valid input. [ 1-4 ] ")
    userInput = int(userInput)
    ##Diagnostic
    if userInput == 1:
        print()
        diagMenu()
        print()
    ##Hardening
    if userInput == 2:
        print()
        print("#####Hardening Menu######")
        print()
        hardMenu()
        print()
    ##About   
    if userInput == 3:
        print()
        print("######About######")
        getAbout()
    

    ##Exit Program
    if userInput == 4:
          return False

    ##Starting run again statement....
    #print()
    #print("Starting Run Again Statement...")
    #print()
    
##Welcome Page
print("########### Welcome to LIT! #############")
print()
print("Pick a function by entering the number you want and pressing ENTER.")
running = True
while running == True:
    running = mainFunction()
    

#Call repeat
#repeat()

