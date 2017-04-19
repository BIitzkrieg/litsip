#!/usr/bin/env python3.5

##Andrew Danis
##Eric Evans
##LIT Protoype
##10-26-16

##################Imports##################
import sys
import os
import time
import subprocess
import platform


##################Functions##################

#  Bool return for a user input integer string
def validInteger(string):
    index = -1
    for char in string:
        index += 1
        if (index == 0 and char[index] == '-' and len(string) > 1):
            continue
        elif not (char in "0123456789"):
            return False
    return True

# Boold return for a user input string
def validAlphabet(string):
    index = -1
    for char in string:
        index += 1
        if (index == 0 and char[index] == '-' and len(string) > 1):
            continue
        elif not (char in "abcdefghijklmnopqrstuvwxyz0123456789"):
            return False
    return True

##Only allows the user to test for functions 1-7
def validInput(string):
    if (string == "1" or string == "2" or string == "3" or string == "4" or string == "5"
        or string == "6" or string == "7"):
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
    if (string == "1" or string == "2" or string == "3" or string == "4" or string == "5" or string == "6"
        or string == "7" or string == "8"):
        return True
    else:
        return False
######################Diagnostic Functions############################################
##print sys info

def sysInfo():
    start = "\033[1m"
    end = "\033[0;0m"
    print("")
    print(start + "Operating System:" + end)
    os.system("uname -a")
    #os.system("lsb_release -a")
    print("")
    print(start + "RAM:" + end)
    os.system("free -h")
    print("")
    print(start + "Partition Info:" + end)
    os.system("df -h")
    print("")
    print(start + "Network Interface Info:" + end)
    os.system("ip addr")
    repeatDiag()

##getTasks
def getTasks():
    print("\nCrontab stands for cron table and is a tool that allows for a list of commands\nto run on a regular schedule."
          " It can be edited through a text editor to do a \nvariety of tasks.\n \nTo find out more visit:")
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
        diagMenu()

##getServices
def getServices():
        print("")
        print("[ 1 ]  Fedora/CentOS")
        print("[ 2 ]  Ubuntu/Debian")
        print("[ 3 ]  Return to Diagnostic Menu")
        print("")
        print("If you don't know your OS select option 3 and go back to the Diagnostic Menu. "
              "Once there select System Info and figure out your OS.")
        print("")
        userInput = input("Choose an OS: ")
        while not validInput3(userInput):
            userInput = input("Please enter a valid input. [ 1-3 ] ")
        userInput = int(userInput)
        ##Fedora/CentOS service check
        if userInput == 1:
            print()
            os.system("systemctl list-unit-files")
            print("")
            repeatDiag()
        ##Ubuntu/Debian Service Check
        if userInput == 2:
            print()
            os.system("service --status-all")
            print("")
            repeatDiag()
        ##IDK my OS return to Diagnostic Menu
        if userInput == 3:
            print()
            diagMenu()

##Get About
def getAbout():
    print("LIT is a Student Innovation Project by Andrew Danis and Zach Evans."
          "Inspired by the common tasks required at the Collegiate Cyber Defense Competition, "
          "LIT is designed to provide the user with an easy to use, navigable script that will help them "
          "easily diagnose and harden their Linux based system. LIT is for both the security and non security "
          "minded people alike, and we hope that the user will be able to learn something along the way.")
    mainFunction()

##getAccounts
def getAccounts():
    print("")
    print("User accounts can be made for use by a human or service/system function in Linux."
          " Select an Option below to view these accounts.")
    print("To find out more about managing user accounts in Linux visit: www.tldp.org/LDP/sag/html/managing-users.html")
    print("")
    print("[ 1 ]  All Accounts")
    print("[ 2 ]  Exclude System/Service Accounts")
    print("[ 3 ]  Return to Diagnostic Menu")
    print("")
    userInput = input("Choose an option: ")
    while not validInput3(userInput):
        userInput = input("Please enter a valid input. [ 1-3 ] ")
    userInput = int(userInput)
    ##Displays all user accounts
    if userInput == 1:
        start = "\033[1m"
        end = "\033[0;0m"
        print("")
        print(start + "###### User Accounts ######" + end)
        print("")
        os.system("cat /etc/passwd")
        print("")
    ##Displays user accounts without nologin or false
    if userInput == 2:
        start = "\033[1m"
        end = "\033[0;0m"
        print("")
        print(start + "###### User Accounts ######" + end)
        print("")
        os.system("cat /etc/passwd | grep -v 'nologin' | grep -v 'false' ")
        print("")
    ##I changed my mind, return to the diagnostic menu
    if userInput == 3:
        print()
        diagMenu()
    repeatDiag()

##getConn
def getConnections():
    print("")
    print("This will show active network connections (TCP and UDP) through the command line network-utility "
          "tool netstat."
          " \n\nTo find out more about your network connections visit: www.netstat.net")
    print("")
    os.system("netstat -tulpn")
    print("")
    repeatDiag()

##exportFile
def exportFile():
    print("")
    print("This function will save all of the Diagnostic Information to a text file in the current directory.")
    print("")
    print("[ 1 ] Save Diagnostic Information")
    print("[ 2 ] Return to Diagnostic Menu")
    print("")
    userInput = input("Choose an option: ")
    while not validInput2(userInput):
        userInput = input("Please enter a valid input. [ 1-2 ] ")
    userInput = int(userInput)
    if userInput == 1:
        print()
        print("\033[1m\033[33mSaving File...\033[0m")
        print()
        print("\033[1m\033[33mType 'cat diagnostic.txt' to read the file once you exit LIT.\033[0m")
        print()
        os.system("printf '\n\033[1m\033[33mOperating System Info: \033[0m\n' > diagnostic.txt "
                  "&& uname -a >> diagnostic.txt "
                  "&& printf '\n\033[1m\033[33mRAM:\033[0m\n' >> diagnostic.txt "
                  "&& free -h >> diagnostic.txt "
                  "&& printf '\n\033[1m\033[33mPartition Info:\033[0m\n' >> diagnostic.txt "
                  "&& df -h >> diagnostic.txt ")
        os.system("printf '\n\033[1m\033[33mNetwork Interface Info:\033[0m\n' >> diagnostic.txt "
                  "&& ip addr >> diagnostic.txt "
                  "&& printf '\n\033[1m\033[33mCrontab:\033[0m\n' >> diagnostic.txt "
                  "&& crontab -l >> diagnostic.txt ")
        os.system("printf '\n\033[1m\033[33mUser Accounts:\033[0m\n' >> diagnostic.txt "
                  "&& cat /etc/passwd >> diagnostic.txt "
                  "&& printf '\n\033[1m\033[33mActive Network Connections:\033[0m\n' >> diagnostic.txt "
                  "&& netstat -tulpn >> diagnostic.txt")
        repeatDiag()
    if userInput == 2:
        print()
        diagMenu()


############################ Hardening Functions ########################################
def changePass():
    print("")
    print("[ 1 ]  Change this accounts password")
    print("[ 2 ]  Change another account")
    print("[ 3 ]  Return to Hardening Menu")
    print("")
    userInput = input("Choose an option: ")
    while not validInput3(userInput):
        userInput = input("Please enter a valid input. [ 1-3 ] ")
    userInput = int(userInput)
    ##Change current acc pass
    if userInput == 1:
        print()
        os.system("passwd")
        repeatHard()
    ##change another account
    if userInput == 2:
        print()
        var = input("Type the name of the account you would like to change: ")
        os.system("passwd " + var)
        hardMenu()
    if userInput == 3:
        print()
        hardMenu()

        repeatHard()

def killServices():
    print("")
    print("[ 1 ]  Enable/Disable Services for Fedora/CentOS")
    print("[ 2 ]  Enable/Disable Services for Ubuntu/Debian")
    print("[ 3 ]  Return to Diagnostic Menu")
    print("")
    print("If you don't know your OS select option 3 and go back to the Diagnostic Menu. "
          "Once there select System Info and figure out your OS.")
    print("")
    userInput = input("Choose an Option: ")
    while not validInput3(userInput):
        userInput = input("Please enter a valid input. [ 1-3 ] ")
    userInput = int(userInput)
    ##Fedora/CentOS service check
    if userInput == 1:
        print()
        time.sleep(5)
        subprocess.call("systemctl list-unit-files", shell=True)
        print()
        print("Services are important to monitor because unnecessary running services "
              "on a machine can make the system more vulnerable to an attack.")
        print()
        print("Would you like to enable or disable a service?")
        print("")
        print("[ 1 ]  Enable")
        print("[ 2 ]  Disable")
        print("[ 3 ]  Return to Hardening Menu")
        print("")
        userInput = input("Choose an Option: ")
        while not validInput3(userInput):
            userInput = input("Please enter a valid input. [ 1-3 ] ")
        userInput = int(userInput)
        if userInput == 1:
            userInput = str(input("Enter the Service you wish to enable: "))
            os.system("systemctl start " + userInput)
            while not validAlphabet(userInput):
                userInput = str(input("Enter a valid integer (Type 'z' to quit): "))
                os.system("systemctl stop " + userInput)
                if userInput.strip() == 'z':
                    break
            repeatHard()
        if userInput == 2:
            userInput = str(input("Enter the Service you wish to disable: "))
            os.system("systemctl stop " + userInput)
            while not validAlphabet(userInput):
                userInput = str(input("Enter a valid integer (Type 'z' to quit): "))
                os.system("systemctl stop " + userInput)
                if userInput.strip() == 'z':
                    break
            repeatHard()
        if userInput == 3:
            repeatHard()
    ##Ubuntu/Debian Service Check
    if userInput == 2:
        print()
        time.sleep(5)
        subprocess.call("service --status-all", shell=True)
        print()
        print("Services are important to monitor because unnecessary running services "
              "on a machine can make the system more vulnerable to an attack.")
        print()
        print("Would you like to enable or disable a service?")
        print("")
        print("[ 1 ]  Enable")
        print("[ 2 ]  Disable")
        print("[ 3 ]  Return to Hardening Menu")
        print("")
        userInput = input("Choose an Option: ")
        while not validInput3(userInput):
            userInput = input("Please enter a valid input. [ 1-3 ] ")
        userInput = int(userInput)
        if userInput == 1:
            userInput = str(input("Enter the Service you wish to enable: "))
            os.system("service " + userInput + " start")
            while not validAlphabet(userInput):
                userInput = str(input("Enter a valid integer (Type 'z' to quit): "))
                os.system("service " + userInput + " stop")
                if userInput.strip() == 'z':
                    break
            repeatHard()
        if userInput == 2:
            userInput = str(input("Enter the Service you wish to disable: "))
            os.system("service " + userInput + " stop")
            while not validAlphabet(userInput):
                userInput = str(input("Enter a valid integer (Type 'z' to quit): "))
                os.system("service " + userInput + " stop")
                if userInput.strip() == 'z':
                    break
            repeatHard()
        if userInput == 3:
            repeatHard()
    ##Return to hardening menu
    if userInput == 3:
        print()
        hardMenu()


def removeAcc():
    print()
    print("Users on a system can be used as an attack platform and should be removed if they aren't in use.")
    print()
    print("[ 1 ]  Remove an Account")
    print("[ 2 ]  Return to Hardening Menu")
    print()
    userInput = input("Choose an option: ")
    while not validInput2(userInput):
        userInput = input("Please enter a valid input. [ 1-2 ] ")
    userInput = int(userInput)
    ##Remove a user account
    if userInput == 1:
        print()
        os.system("cat /etc/passwd | grep -v 'nologin' | grep -v 'false' ")
        print()
        accountname = str(input("Enter the user account name: "))
        if accountname.isalnum():
            start = "\033[1m"
            end = "\033[0m"
            print("")
            os.system("userdel -r -f " + accountname)
            print("")
            print(start + "User removed!" + end)
            print("")
            repeatHard()
        if not accountname.strip():
            start = "\033[1m"
            end = "\033[0m"
            print()
            print(start + "Enter a valid user!" + end)
            removeAcc()
    ##Return to hardening menu
    if userInput == 2:
        print()
        hardMenu()

def killConnections():
    print()
    print("[ 1 ]  Begin Killing Specific Network Connections")
    print("[ 2 ]  Return to Hardening Menu")
    print()
    print("This function will show active network connections (TCP and UDP) through "
          "the command line network-utility tool netstat. There may undesired connections being made, selecting to kill"
          " the connection can help eliminate a possible threat to the current system.")
    print()
    userInput = input("Choose an option: ")
    while not validInput2(userInput):
        userInput = input("Please enter a valid input. [ 1-2 ] ")
    userInput = int(userInput)
    if userInput == 1:
        print()
        #'"www.crontab.org"\n'
        print("The active connections will be presented. Note the PID of the connection you want to kill, press "'"q"'" to "
          "quit, you will be prompted to kill that PID.")
        print()
        time.sleep(5)
        subprocess.call('netstat -tulpn', shell=True)
        print()
        userInput = str(input("Enter the PID you wish to kill: "))
        os.system("kill " + userInput)
        while not validInteger(userInput):
            userInput = str(input("Enter a valid integer (Type 'z' to quit): "))
            os.system("kill " + userInput)
            if userInput.strip() == 'z':
                break
        repeatHard()
    if userInput == 2:
        repeatHard()

def killProc():
    print()
    print("[ 1 ]  Begin Killing Specific Processes")
    print("[ 2 ]  Return to Hardening Menu")
    print()
    print("This function will show the actively running processes on the system and under which user they are being run"
          ". The process id or PID will be shown and you can choose to kill a process or not. Viewing the processes "
          "will allow you to lock down your system by deciding what you want to be running. ")
    print()
    userInput = input("Choose an option: ")
    while not validInput2(userInput):
        userInput = input("Please enter a valid input. [ 1-2 ] ")
    userInput = int(userInput)
    if userInput == 1:
        print()
        #'"www.crontab.org"\n'
        print("The process manager will be spawned...Note the PID of the process you want to kill, press "'"q"'" to quit, "
          "and you will be prompted to kill that PID.")
        print()
        time.sleep(5)
        subprocess.call('ps aux | less', shell=True)
        print()
        userInput = str(input("Enter the PID you wish to kill: "))
        os.system("kill " + userInput)
        while not validInteger(userInput):
            userInput = str(input("Enter a valid integer (Type 'z' to quit): "))
            os.system("kill " + userInput)
            if userInput.strip() == 'z':
                break
        repeatHard()
    if userInput == 2:
        repeatHard()

def getTools():
    print("[ 1 ]  Install ClamAV")
    print("[ 2 ]  Install Lynis")
    print("[ 3 ]  Return to Main Menu")
    print("")
    userInput = input("Choose an option: ")
    while not validInput3(userInput):
        userInput = input("Please enter a valid input. [ 1-3 ] ")
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

    if userInput == 3:
        mainFunction()

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

##function to repeat hardMenu
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
            
#############Menus#########################    
def diagMenu():
    start = "\033[1m"
    end = "\033[0;0m"
    print()
    print(start + "######## Diagnostic Menu ########" + end)
    print()
    print("[ 1 ]  System Info")
    print("[ 2 ]  Scheduled Tasks")
    print("[ 3 ]  Enabled/Running Services")
    print("[ 4 ]  Display User Accounts")
    print("[ 5 ]  Display Active Connections")
    print("[ 6 ]  Export Diagnostic Information")
    print("[ 7 ]  Return to Main Menu")
    print("[ 8 ]  Exit")
    print()
    userInput = input("Pick a function to run: ")
    while not validInput8(userInput):
        userInput = input("Please enter a valid input. [ 1-8 ] ")
    userInput = int(userInput)
    ##Call Sys Info
    if userInput == 1:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "##### System Info ######" + end)
        sysInfo()
        print()
    ##Call Scheduled Tasks
    if userInput == 2:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "#### Scheduled Tasks ######" + end)
        getTasks()
    ##Call Services   
    if userInput == 3:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "###### Enabled/Running Services ######" + end)
        getServices()
    ##Call Accounts  
    if userInput == 4:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "###### User Accounts ######" + end)
        getAccounts()
    ##Call Active Connections  
    if userInput == 5:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "###### Active Connections ######" + end)
        getConnections()
    ##Call Export Diagnostic Information
    if userInput == 6:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "###### Export Diagnostic Information ######" + end)
        exportFile()
    ##Call Menu   
    if userInput == 7:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "###### We're Going Back Marty ######" + end)
        mainFunction()

    ##Exit Program
    if userInput == 8:
        return False

def hardMenu():
    start = "\033[1m"
    end = "\033[0;0m"
    print()
    print(start + "######## Hardening Menu ########" + end)
    print()
    print("[ 1 ]  Change Account Password")
    print("[ 2 ]  Enable/Disable Services")
    print("[ 3 ]  Remove User Accounts")
    print("[ 4 ]  Kill Active Connections")
    print("[ 5 ]  Kill Active Processes")
    print("[ 6 ]  Return to Main Menu")
    print("[ 7 ]  Exit")
    print()
    userInput = input("Pick a function to run: ")
    while not validInput(userInput):
        userInput = input("Please enter a valid input. [ 1-7 ] ")
    userInput = int(userInput)
    ##Call changePass
    if userInput == 1:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "##### Change Account Password ######" + end)
        changePass()
        print()
    ##Call killServices
    if userInput == 2:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "###### Kill/Disable Services ######" + end)
        killServices()
    ##Call removeAcc
    if userInput == 3:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "###### Remove User Accounts ######" + end)
        removeAcc()
    ##Call killConnections
    if userInput == 4:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "###### Kill Active Connections ######" + end)
        killConnections()
    ##Call killProc
    if userInput == 5:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "###### Kill Active Processes ######" + end)
        killProc()
    ##Returns to Main Menu
    if userInput == 6:
        start = "\033[1m"
        end = "\033[0;0m"
        print()
        print(start + "####### We're Going Back Marty! ######" + end)
        mainFunction()

    ##Exit Program
    if userInput == 7:
        return False
           

##################Print Statements/Input/Main##################
##Main Menu
def mainFunction():
    start = "\033[1m"
    end = "\033[0;0m"
    print()
    print(start + "######## Main Menu ########" + end)
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
        print("\033[1m###### About ######\033[0m")
        print()
        getAbout()

    ##Exit Program
    if userInput == 5:
          return False

def onStart():

    euid = os.geteuid()
    if euid != 0:
        print("Script not started as root. Running sudo..")
        args = ['sudo', sys.executable] + sys.argv + [os.environ]
        # the next line replaces the currently-running process with the sudo
        os.execlpe('sudo', *args)
    print()
    print('Running with privileges.')
    print()
    #print("Getting dependencies...")
    #os.system("t)
    
##Welcome Page
start = "\033[31m"
end = "\033[0;0m"
print()

print(start + "#########################################" + end)
print("\033[31m###########\033[0;0m " "\033[1m\033[37mWelcome to LIT!\033[0;0m" " \033[31m#############\033[0;0m")
print(start + "#########################################" + end)
print()
print("Pick a function by entering the number you want and pressing ENTER.")
running = True
while running == True:

    running = onStart(),mainFunction()

    

#Call repeat
#repeat()

