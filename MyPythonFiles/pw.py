#! /usr/bin/env python3

"""
#pw.py - An insecure paswword locker program

Title: PasswordManagerSoftware
Problem: having different accounts using one password make it easy for hackers
hack your accounts.
Solution: desiging a password manager software that uses one master pasword
to unlock the password manager.
--------------------------------------------------------------------------------
User Experience:
0. run the prorgam in terminal in three steps:
 0.1. Make the prorgam executable (chmod +x pythonScript.py) 
 0.2. Call the program (e.g. /pythonScript.py)
 0.3. ran the program for the account that requires its password (e.g. /pythonScript.py email)
 
1. see a message "copy your account password to the clipboard"
2. See the password on clipboard (Two notes:
2.1. Computer will copy the account paswword to the clipboard)
2.2. In Mac, one can have access to clipboard by clicking on "Finder", then "Edit", and finly "show clipboard"
Find the way of seeing the clipboard for your computer.
3. Paste the password from the clipboard into the website's pasword field
----------------------------------------------------------------------------------------------------
Instructions to Computer:
1. store account names and their passwords in a "Dictionary" data type
(why using Dictionary? to associate each account's name with its password)
2. store account name as a string in a variable "account"

3. import sys library
We import sys because it enables the command line argument to be stored in a variable sys.argv
- sys.argv is a list
- the first item in sys.argv is program's file name (e.g. 'pw.py')
- sys.argv is the list of commandline arguments passed to the Python program.
argv represents all the items that come along via the commandline input
it's basically an array holding the command line arguments of our program.

4. check if the account name exists in the PASSWORD dictionary as a key
4.1. If the account name exists in the PASSWORD dictionary as a key,
then print the key value to clipboard (using pyperclip.copy)
    4.1.1. Note: to use the pyperclip.copy we need to import the module
4.2.If the account name DOES NOT exist in the PASSWORD dictionary as a key,
then print a message that "there is not an account with this name'
"""

PASSWORDS = {'dropbox-gmail': 'Parastoo1',
             'dropbox-brunel': 'Trp12des',
             'Jupyterhub': 'Parastoo2Parastoo2',
             'CamStudentEmail': '.Trp12des',
             }

print('run the program and type the account for which you want its password')
import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    














