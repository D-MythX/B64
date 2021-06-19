#!/usr/bin/env python3
#Title: Base64 encoder & decoder
#Author: MY7H

import os
import time

y = "\033[2;33m"
g = "\033[2;32m"
p = "\033[2;35m"
w = "\033[2;37m"
e = "\033[0m"

os.system("clear")
print(g+"["+w+"~"+g+"]"+y+" GETTING REQUIREMENTS!!!..\n"+e)
time.sleep(0.5)
os.system("cd $home")
os.system("apt update")
os.system("apt upgrade -y")
os.system("apt install python -y")
os.system("apt install figlet -y")
os.system("apt install git -y")
os.system("apt install ruby -y")
os.system("gem install lolcat")
os.system("clear")
os.system("cd B64")
print(g+"["+w+"✓"+g+"]"+y+" COMPLETED!!!\n")
time.sleep(1.0)
print(g+"["+w+"~"+g+"]"+y+" AUTOMATICALLY LAUNCHING TOOL IN 7secs...")
print(g+"\n>>"+y+" Run the tool manually next time with\n          ~"+p+" python b64.py "+y+"~")
time.sleep(7.0)
os.system("python b64.py")
