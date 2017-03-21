#!/usr/bin/env python3

##Andrew Danis
##Eric Evans
##LIT Protoype
##10-26-16

##################Imports##################
import sys
import os
import subprocess


##################Functions##################
## Bool return for a user input integer string
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

##Only allows the user to test for functions 1-2 for getServices
def validInput2(string):
    if (string == "1" or string == "2"):
        return True
    else:
        return False

def validInput3(string):
    if (string == "1" or string == "2" or string == "3"):
        return True
    else:
        return False

##Only allows the user to test for functions 1-5 for Main Menu
def validInput5(string):
    if (string == "1" or string == "2" or string == "3" or string == "4" or string == "5"):
        return True
    else:
        return False

##Only allows the user to test for functions 1-8 for hardeningMenu
def validInput8(string):
    if (string == "1" or string == "2" or string == "3" or string == "4" or string == "5" or string == "6" or string == "7" or string == "8"):
        return True
    else:
        return False
######################Diagnostic Functions############################################3
##print sys info
def sysInfo():
    os.system("lsb_release -a; free -m;  df -h; ifconfig")
    repeatDiag()
    
    
##getTasks
def getTasks():
    print("\nCrontab stands for cron table and is a tool that allows for a list of commands\nto run on a regular schedule. It can be edited through a text editor to do a \nvariety of tasks.\n \nTo find out more visit:")
    print('"www.crontab.org"\n')
    print("[ 1 ]  Edit Crontab")
    print("[ 2 ]  Return to Diagnostic Menu\n")
    userInput = input("Choose an option: ")
    while not validInput2(userInput):
        userInput = input("Please enter a valid input. [ 1-2 ] ")
    userInput = int(userInput)
    if userInput == 1:
        print()
        os.system("crontab -e")
        repeatDiag()
    if userInput == 2:
        print()
        repeatDiag()
    

##getServices
def getServices():
        print("[ 1 ]  Fedora/CentOS")
        print("[ 2 ]  Ubuntu/Debian")
        userInput = input("Choose an OS: ")
        while not validInput2(userInput):
            userInput = input("Please enter a valid input. [ 1-2 ] ")
        userInput = int(userInput)
        ##Fedora/CentOS service check
        if userInput == 1:
            print()
            os.system("systemctl list-unit-files")
            repeatDiag()
        ##Ubuntu/Debian Service Check
        if userInput == 2:
            print()
            os.system("service --status-all")
            repeatDiag()


##Get About
def getAbout():
    print('%-200s'%"LIT is a Student Innovation Project by Andrew Danis and Zach Evans.\nInspired by the common tasks required at the Collegiate Cyber Defense Competition, LIT is designed to provide the user with an easy to use, navigable script that will help them easily diagnose and harden their Linux based system.\nLIT is for both the security and non security minded people alike, and we hope that the user will be able to learn something along the way.")    
    mainFunction()
##getAccounts
def getAccounts():
    os.system("cat /etc/passwd")
    repeatDiag()
##getConn
def getConnections():
    os.system("netstat -tulpn")
    repeatDiag()
############################ Hardening Functions ########################################
def changePass():
    print("[ 1 ]  Change this accounts password")
    print("[ 2 ]  Change another account")
    userInput = input("Choose an option: ")
    while not validInput2(userInput):
        userInput = input("Please enter a valid input. [ 1-2 ] ")
    userInput = int(userInput)
    ##Change current acc pass
    if userInput == 1:
        print()
        os.system("passwd")
        repeatHard()
    ##change another account
    if userInput == 2:
        print()
        print("Type 'passwd' then the name of the account you would like to change")
        os.system("")
        repeatHard()
## def removeTasks():

#def killServices():

#def removeAcc():

#def killConnections():

#def killProc():

def getTools():
    print("[ 1 ]  Install ClamAV")
    print("[ 2 ]  Install Lynis")
    userInput = input("Choose an option: ")
    while not validInput2(userInput):
        userInput = input("Please enter a valid input. [ 1-2 ] ")
    userInput = int(userInput)
    ##Change current acc pass
    if userInput == 1:
        print()
        print("[ 1 ]  Fedora")
        print("[ 2 ]  CentOS")
        print("[ 3 ]  Ubuntu/Debian")
        userInput = input("Choose an OS: ")
        while not validInput3(userInput):
            userInput = input("Please enter a valid input. [ 1-3 ] ")
        userInput = int(userInput)
        if userInput == 1:
            os.system("dnf install clamav")
        if userInput == 2:
            os.system("yum install clamav")
        if userInput == 3:
            os.system("apt-get install clamav")
    ##change another account
    if userInput == 2:
        print()
        print("[ 1 ]  Fedora")
        print("[ 2 ]  CentOS")
        print("[ 3 ]  Ubuntu/Debian")
        userInput = input("Choose an OS: ")
        while not validInput3(userInput):
            userInput = input("Please enter a valid input. [ 1-3 ] ")
        userInput = int(userInput)
        if userInput == 1:
            os.system("dnf install lynis")
        if userInput == 2:
            os.system("yum install lynis")
        if userInput == 3:
            os.system("apt-get install lynis")


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

def repeatHard():
    daddy = False
    while True:
        response = input("Would you like to return to the Hardening menu? (y/n) ").lower()
        if response in ['n', 'no']:
            print("Exiting...")
            sys.exit()
        elif response in ['y', 'yes']:
            print("Going to Menu")
            hardMenu()
            return daddy
        else:
            print("Invalid input.. ")

##
def symbolInfo():
        print('hi')
        
            
#############Menus#########################    
def diagMenu():
    print()
    print("######## Diagnostic Menu ########")
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
        print("##### System Info ######")
        sysInfo()
        print()
    ##Call Scheduled Tasks
    if userInput == 2:
        print()
        print("#### Scheduled Tasks ######")
        getTasks()
    ##Call Services   
    if userInput == 3:
        print()
        print("###### Enabled/Running Services ######")
        getServices()
    ##Call Accounts  
    if userInput == 4:
        print()
        print("###### User Accounts# #####")
        getAccounts()
    ##Call Active Connections  
    if userInput == 5:
        print()
        print("###### Active Connections ######")
        getConnections()
    ##Call Menu   
    if userInput == 6:
        print()
        print("###### We're Going Back Marty ######")
        mainFunction()

    ##Exit Program
    if userInput == 7:
          return False

def hardMenu():
    print()
    print("######## Hardening Menu ########")
    print()
    print("[ 1 ]  Change Account Password")
    print("[ 2 ]  Remove Scheduled Tasks")
    print("[ 3 ]  Kill/Disable Services")
    print("[ 4 ]  Remove User Accounts")
    print("[ 5 ]  Kill Active Connections")
    print("[ 6 ]  Kill Active Processes")
    print("[ 7 ]  Return to Main Menu")
    print("[ 8 ]  Exit")
    print()
    userInput = input("Pick a function to run: ")
    while not validInput8(userInput):
        userInput = input("Please enter a valid input. [ 1-8 ] ")
    userInput = int(userInput)
    ##Call changePass
    if userInput == 1:
        print()
        print("##### Change Account Password ######")
        changePass()
        print()
    ##Call removeTasks
    if userInput == 2:
        print()
        print("#### Remove Scheduled Tasks ######")
        removeTasks()
    ##Call killServices
    if userInput == 3:
        print()
        print("###### Kill/Disable Services ######")
        killServices()
    ##Call removeAcc
    if userInput == 4:
        print()
        print("###### Remove User Accounts ######")
        removeAcc()
    ##Call killConnections
    if userInput == 5:
        print()
        print("###### Kill Active Connections ######")
        killConnections()
    ##Call killProc
    if userInput == 6:
        print()
        print("###### Kill Active Processes ######")
        killProc()

    if userInput == 7:
        print()
        print("####### We're Going Back Marty! ######")
        mainFunction()
    ##Exit Program
    if userInput == 8:
        return False
           

##################Print Statements/Input/Main##################
##Main Menu
def mainFunction():
    print()
    print("######## Main Menu ########")
    print()
    print("[ 1 ]  Diagnostic Menu")
    print("[ 2 ]  Hardening Menu")
    print("[ 3 ]  Install Useful Tools")
    print("[ 4 ]  About")
    print("[ 5 ]  Exit")
    print()
    userInput = input("Pick a function to run: ")
    while not validInput5(userInput):
        userInput = input("Please enter a valid input. [ 1-5 ] ")
    userInput = int(userInput)
    ##Diagnostic
    if userInput == 1:
        print()
        diagMenu()
        print()
    ##Hardening
    if userInput == 2:
        print()
        hardMenu()
        print()
    ##Install Tools
    if userInput == 3:
        print()
        getTools()
    ##About   
    if userInput == 4:
        print()
        print("###### About ######")
        getAbout()

    

    ##Exit Program
    if userInput == 5:
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

