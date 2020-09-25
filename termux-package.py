#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[91m
 .----------------------------------------------------------------------.
  |_.-._.-._.-._.-._.-._.-.    _.-._.-._.-.    _.-._.-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-._. .::db .-._.-._. .::db .-._.-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-._ .::d88b -._.-._ .::d88b -._.-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-. .::d8888b       .::d8888b ._.-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.- .::d88!::::::::::::d888888b _.-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.- \  Y88\_________\  Y888888P _.-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-. \  Y8888P ._.-. \  Y8888P ._.-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-._ /dbY88Pdb _.-._ /dbY88Pdb _.-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-. /d8P_YP Y8b .-. /d8P_YP Y8b .-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-     /d8P .-.\ Y8b   /d8P .- \ Y8b -._.-._.-._.-._.-._.|
  |_.-._.-._.-._ .::db/d8P _.-. \.::db/d8P _.-. \ Y8b ._.-._.-._.-._.-._.|
  |_.-._.-._.-. .::d88bYP ._.-. .::d88LSP ._.-._ \ Y8b    ._.-._.-._.-._.|
  |_.-._.-._.- .::d8888b       .::d8888b`b _.-._. \ Y8b:db _.-._.-._.-._.|
  |_.-._.-._. .::d88!::::::::::::d888888b`b .-._.- \ YPd88b .-._.-._.-._.|
  |_.-._.-._. \  Y88\_________\  Y888888Pd8b       .::d8888b -._.-._.-._.|
  |_.-._.-._.- \  Y8888P -._.- \  Y8888P!::::::::::::d888888b ._.-._.-._.|
  |_.-._.-._.-. \  Y88Pdb ._.-. \  Y88Pdb_________\  Y888888P ._.-._.-._.|
  |_.-._.-._.-._ \__YP Y8b _.-._ \__YP Y8b`P -._.- \  Y8888P -._.-._.-._.|
  |_.-._.-._.-._.-._. \ Y8b .-._.-. /d\ Y8b .-._.-. /dbY88P .-._.-._.-._.|
  |_.-._.-._.-._.-._.- \ Y8b -._.- /d8P\ Y8b -._.- /d8P_YP _.-._.-._.-._.|
  |_.-._.-._.-._.-._.-. \ Y8b     /d8P _\ Y8b     /d8P _.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-._ \ Y8b:db/d8P ._ \ Y8b:db/d8P ._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-._. \ YPd88bYP -._. \ YPd88bYP -._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-._. .::d8888b       .::d8888b .-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-._ .::d88!::::::::::::d888888b -._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-._ \  Y88\_________\  Y888888P -._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-._. \  Y8888P .-._. \  Y8888P .-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-._.- \  Y88P _.-._.- \  Y88P _.-._.-._.-._.-._.-._.|
  |_.-._.-._.-._.-._.-._.-. \__YP ._.-._.-. \__YP ._.-._.-._.-._.-._.-._.|
  `----------------------------------------------------------------------'

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
| Coded By Nitro Hacker|version : 2.5  |
+--------------------------------------+''')

slowprint(''' \033[93m
[01] python
[02] python2
[03] python-dev
[04] python3
[05] php
[06] java
[07] git
[08] perl
[09] bash
[10] nano
[11] curl
[12] openssl
[13] openssh
[14] wget
[15] clang
[16] nmap
[17] w3m
[18] hydra
[19] ruby
[20] macchanger
[21] host
[22] dnsutils
[23] coreutils
[24] wireshark
[25] wcalc
[26] bmon
[27] vpn
[29] unrar
[30] toilet
[31] proot
[32] net-tools
[33] golang
[34] chroot
[35] cmarix
[36] host
[37] havij
[38] figlet
[39] cowsay
[40] zip
[41] unzip
[42] tor
[43] google
[44] lolcat
[45] fish
[45] help
[46] tar
[47] vim''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")
os.system ("atp upgrade -y")
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
os.system ("apt install wireshark -y")
os.system ("apt install wcalc -y")
os.system ("apt install bmon -y")
os.system ("apt install vpn -y")
os.system ("apt install unrar -y")
os.system ("apt install toilet -y")
os.system ("apt install proot -y")
os.system ("apt install net-tools -y")
os.system ("apt install golang -y")
os.system ("apt install chroot -y")

os.system ("apt install cmatrix -y")
os.system ("apt install host -y")
os.system ("apt install havij -y")
os.system ("apt install figlet -y")
os.system ("apt install tar -y")
os.system ("apt install zip -y")
os.system ("apt install unzip -y")
os.system ("apt install tor -y")
os.system ("apt install google -y")
os.system ("apt install lolcat -y")
os.system ("apt install fish -y")
os.system ("apt install vim -y")


print ("""
subscribe Nitro Hacker""")

os.system ("apt install ruby -y")
os.system ("apt install macchanger -y")
os.system ("apt install host -y")
os.system ("apt install dnsutils -y")
os.system ("apt install coreutils -y")

print ("Allow the Button For Access the Storage in Termux")


os.system ("termux-setup-storage")

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|             Welcome To Hackers World            |
|           Subscribe Our YouTube Channel         |
| Watch Ours Tutorials For Learn Ethical Hacking  |''')
print("+-------------------------------------------------+")

input("\n\nPress the enter key to exit : ")
