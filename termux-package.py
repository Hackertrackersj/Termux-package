#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[91m
    _____ ___ ___ __  __ _   ___  __  ___  _   ___ _  __   _   ___ ___ 
  |_   _| __| _ \  \/  | | | \ \/ / | _ \/_\ / __| |/ /  /_\ / __| __|
    | | | _||   / |\/| | |_| |>  <  |  _/ _ \ (__| ' <  / _ \ (_ | _| 
    |_| |___|_|_\_|  |_|\___//_/\_\ |_|/_/ \_\___|_|\_\/_/ \_\___|___|                                                                       
                                                                                                                                                                                                                              
CREATED BY NITRO HACKER
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[95m
+--------------------------------------+
| This Tool Install All Basic Packages |
+--------------------------------------+
| Coded By Nitro Hacker|version : 2.3  |
+--------------------------------------+''')

slowprint(''' \033[93m
[01] python-dev
[02] python3
[03] php
[04] java
[05] git
[06] perl
[07] bash
[08] nano
[09] curl
[10] openssl
[11] openssh
[12] wget
[13] clang
[14] nmap
[15] w3m
[16] hydra
[17] ruby
[18] macchanger
[19] host
[20] dnsutils
[21] coreutils
[22] fish
[23] zip
[24] tor
[25] hydra
[26] figlet 
[27] cowsay
[28] tar
[29] unzip
[30] vim
[31] ruby
[32] wcalc
[33] bmon
[34] unrar
[35] proot
[36] golang''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")
os.system ("apt upgrade -y")
os.system ("apt install python -y")
os.system ("apt install python2 -y")
os.system ("apt install php -y")
os.system ("apt install python-dev -y")
os.system ("apt install python3 -y")
os.system ("apt install java -y")
os.system ("apt install git -y")
os.system ("apt install perl -y")
os.system ("apt install bash")

print ("wait for second and start hacking")

os.system ("apt install nano -y")
os.system ("apt install curl -y")
os.system ("apt install openssl -y")
os.system ("apt install openssh -y")
os.system ("apt install wget -y")
os.system ("apt install clang -y")
os.system ("apt install nmap -y")
os.system ("apt install w3m -y")
os.system ("apt install hydra -y")


print ("""
subscribe Nitro Hacker""")

os.system ("apt install ruby -y")
os.system ("apt install macchanger -y")
os.system ("apt install host -y")
os.system ("apt install dnsutils -y")
os.system ("apt install coreutils -y")
os.system ("apt install fish -y")
os.system ("apt install zip -y")
os.system ("apt install hydra -y")
os.system ("apt install figlet -y")
os.system ("apt install cowsay -y")
os.system ("apt install unzip -y")
os.system ("apt install vim -y")
os.system ("apt install ruby -y")
os.system ("apt install wcalc -y")
os.system ("apt install bmon -y")
os.system ("apt install unrar -y")
os.system ("apt install proot -y")
os.system ("apt install golang -y")
print ("Allow the Button For Access the Storage in Termux")


os.system ("termux-setup-storage")
  
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|             Welcome To NITRO HACKER           |
|           Subscribe Our YouTube Channel         |
| Watch Ours Tutorials For Learn Ethical Hacking  |''')
print("+-------------------------------------------------+")


input("\n\nPress the enter key to exit : ")
