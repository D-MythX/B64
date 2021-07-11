#!/usr/bin/env python3
#coding: utf-8
#Title: Base64 encoder & decoder
#Author: MY7H

import os
import time

y = "\033[2;33m"
g = "\033[1;30m"
p = "\033[2;32m"
w = "\033[2;37m"
e = "\033[0m"

os.system("clear")
print(g+"---["+w+"~"+g+"]"+y+" GETTING REQUIREMENTS;!!..\n"+e)
time.sleep(0.5)
os.system("cd $home && apt install python -y && apt install figlet -y && apt install git -y && apt install ruby -y && gem install lolcat && git clone https://github.com/D-MythX/B64 && clear && cd B64")
print(g+"\n---["+w+"✓"+g+"]"+y+" COMPLETED!!!\n")
time.sleep(1.0)
print(g+"---["+w+"~"+g+"]"+y+" AUTOMATICALLY LAUNCHING TOOL IN 7secs...")
print(g+"\n    >>"+y+" Run the tool manually next time with\n\n               ~"+p+" python b64.py "+y+"~")
time.sleep(7.0)
os.system("python b64.py")
