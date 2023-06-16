#!/usr/bin/env python3

import os
import colorama
from colorama import Fore, Style

colorama.init()

os.system('pkg install figlet')
os.system('clear')
os.system('figlet BlackRose')
print('''
---------------------------------------------------------
Termux Installation Tool        powered == By BlackRosepy
---------------------------------------------------------

1) All Termux Commands
2) Exit Tool
''')

choice = input(Fore.YELLOW + 'Enter the operation number: ' + Style.RESET_ALL)

if choice == '1':
    proceed = input(Fore.YELLOW + 'Do you want to start the installation? (Y/N): ' + Style.RESET_ALL)
    if proceed.lower() == 'y':
        print(Fore.CYAN + 'INSTALLATION IN PROGRESS.................' + Style.RESET_ALL)
        os.system('pkg install sl')
        os.system('pkg install git -y')
        os.system('clear')
        os.system('pkg install python python2 python3 -y')
        os.system('clear')
        os.system('pkg install wget -y')
        os.system('clear')
        os.system('pkg install curl -y')
        os.system('clear')
        os.system('pkg install tmux')
        os.system('clear')
        os.system('pkg install ruby -y')
        os.system('clear')
        os.system('pkg install php -y')
        os.system('clear')
        os.system('pkg install pip pip2 -y')
        os.system('clear')
        os.system('pip install colorama -y')
        os.system('clear')
        os.system('pip install telethon -y')
        os.system('clear')
        os.system('pip install --upgrade pip -y')
        os.system('clear')
        os.system('pkg install clang -y')
        os.system('clear')
        os.system('pkg install vim -y')
        os.system('clear')
        os.system('pkg install nano -y')
        os.system('clear')
        os.system('apt install proot -y')
        os.system('clear')
        os.system('pkg install cat -y')
        os.system('clear')
        os.system('pkg install figlet -y')
        os.system('clear')
        os.system('pkg install cmatrix -y')
        os.system('clear')
        os.system('pkg install perl -y')
        os.system('clear')
        os.system('pkg install nmap -y')
        os.system('clear')
        os.system('pkg install openssl -y')
        os.system('clear')
        os.system('pkg install nodejs -y')
        os.system('clear')
        os.system('pkg install wordlist -y')
        os.system('clear')
        os.system('apt install curl -y')
        os.system('clear')
        os.system('apt upgrade -y')
        os.system('clear')
        os.system('apt install dnsutils -y')
        os.system('clear')
        os.system('pip install wordlist -y')
        os.system('clear')
        os.system('apt install bash -y')
        os.system('clear')
        os.system('apt install nodejs -y')
        os.system('clear')
        os.system('pip install requests -y')
        os.system('clear')
        os.system('apt install clang -y')
        os.system('clear')
        os.system('apt install jq -y')
        os.system('clear')
        os.system('apt install macchanger -y')
        os.system('clear')
        os.system('apt install tar -y')
        os.system('clear')
        os.system('apt install zip -y')
        os.system('clear')
        os.system('apt install unzip -y')
        os.system('clear')
        os.system('apt install tor -y')
        os.system('clear')
        os.system('apt install wget -y')
        os.system('clear')
        os.system('apt install wcalc -y')
        os.system('clear')
        os.system('apt install openssl')
        os.system('clear')
        os.system('apt install bmon -y')
        os.system('clear')
        os.system('pkg upgrade -y')
        os.system('pkg update -y')
        os.system('clear')
        os.system('sl')
        os.system('clear')
        os.system('figlet BlackRose')
        print('''
--------------------------------------------------------
Termux Installation Tool        Create == By BlackRosepy
--------------------------------------------------------
''')
        print('')
        print(Fore.YELLOW + 'INSTALLATION COMPLETED :)'+ Style.RESET_ALL)
    else:
        print(Fore.RED + 'Invalid choice. Exiting the tool...' + Style.RESET_ALL)
        exit()

elif choice == '2':
    exit_tool = input(Fore.YELLOW + 'PRESS ENTER TO EXIT THE TOOL' + Style.RESET_ALL)
    exit()

else:
    print(Fore.RED + 'Invalid choice. Exiting the tool...' + Style.RESET_ALL)
    exit()
