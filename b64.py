#!/usr/bin/env python3
#Title: Base64 encoder & decoder
#Author: MY7H

import os
import base64
import time

y = "\033[2;33m"
g = "\033[1;30m"
p = "\033[2;32m"
w = "\033[2;37m"
r = "\033[2;31m"
e = "\033[0m"
u = "\033[4m"
B = "\033[2;01m"

def banner():
    os.system('clear')
    version = g+"v2.1"+e
    Author = r+"MY7H"+e
    print(p+"""
          __________  ________   _____  
          \______   \/  _____/  /  |  | 
           |    |  _/   __  \  /   |  |_
           |    |   \  |__\  \/    ^   /
           |______  /\_____  /\____   | 
             """+version+p+""" \/       \/      |__|["""+Author+p+"""]
    """)
    print(p+"~ Base64 Encoder and Decoder for Texts and Images ~")
    
def enc(text):
    text_byte = text.encode('ascii')
    text_encode = base64.b64encode(text_byte) 
    text_b64 = text_encode.decode('ascii')
    time.sleep(0.5)
    print(g+"\n        ---["+w+"✓"+g+"]"+y+" Encoded to:\n\n["+p,text_b64,y+"]")
    input(g+"\n["+y+"ENTER"+g+"]")
    
def txtEnc(text):
    text_byte = text.encode('ascii')
    text_encode = base64.b64encode(text_byte) 
    text_b64 = text_encode.decode('ascii')
    time.sleep(0.5)
    x = input(g+"\n---["+w+"?"+g+"]"+y+" What would you want to be the title of your Text_File? "+g+"")
    file = open("/sdcard/Android/"+x+"Enc.txt", 'w')
    file.write(text_b64)
    file.close()
    time.sleep(0.5)
    print(g+"\n"+g+"        ---["+w+"✓"+g+"]"+y+" Saved to:\n    ["+g+"Storage"+y+" >> "+g+"Android "+w+">>"+g+" "+x+"Enc.txt"+y+"]")
    input(g+"\n["+y+"ENTER"+g+"]")

def saveEncImage(text):
    time.sleep(0.5)
    x = input(g+"\n---["+w+"?"+g+"]"+y+" What would you want to be the title of your Image_txtFile? "+g+"")
    file = open("/sdcard/Android/"+x+"Enc.txt", 'wb')
    file.write(text)
    file.close()
    time.sleep(0.5)
    print(g+"\n        ---["+w+"✓"+g+"]"+y+" Saved to:\n     ["+g+"Storage "+y+">> "+g+"Android "+y+">>"+g+" "+x+"Enc.txt"+y+"]")
    input(g+"\n["+y+"ENTER"+g+"]")

def dec(text):
    text_byte = text.encode('ascii')
    text_encode = base64.b64decode(text_byte) 
    text_b64 = text_encode.decode('ascii')
    time.sleep(0.5)
    print(g+"\n        ---["+w+"✓"+g+"]"+y+" Decoded to:\n\n["+p,text_b64,y+"]")
    input(g+"\n["+y+"ENTER"+g+"]")
    
def txtDec(text):
    text_byte = text.encode('ascii')
    text_encode = base64.b64decode(text_byte) 
    text_b64 = text_encode.decode('ascii')
    time.sleep(0.5)
    x = input(g+"\n---["+w+"?"+g+"]"+y+" What would you want to be the title of your Text_File? "+g+"")
    file = open("/sdcard/Android/"+x+"Dec.txt", 'w')
    file.write(text_b64)
    file.close()
    time.sleep(0.5)
    print(g+"\n        ---["+w+"✓"+g+"] "+y+"Saved to:\n     ["+g+"Storage "+y+">> "+g+"Android "+y+">>"+g+" "+x+"Dec.txt"+y+"]")
    input(g+"\n["+y+"ENTER"+g+"]")

def saveDecImage(text):
    time.sleep(0.5)
    x = input(g+"\n---["+w+"?"+g+"] "+y+"What would you want to be the title of your Decoded Image?"+g+" ")
    file = open("/sdcard/Android/"+x+"Dec.jpg", 'wb')
    file.write(text)
    file.close()
    time.sleep(0.5)
    print(g+"\n        ---["+w+"✓"+g+"]"+y+" Saved to:\n     ["+g+"Storage "+y+">>"+g+" Android "+y+">>"+g+" "+x+"Dec.jpg"+y+"]")
    input(g+"\n["+y+"ENTER"+g+"]") 


while True:
    banner()
    choice = input(g+"\n    ---["+w+"*"+g+"]"+y+" Pick Option:\n"+g+"    ---["+w+"1"+g+"]"+y+" Encode\n"+g+"    ---["+w+"2"+g+"]"+y+" Decode\n"+g+"    ---["+w+"3"+g+"]"+y+" Update tool\n"+g+"    ---["+w+"4"+g+"]"+r+" Exit\n\n"+g+"    ---»»"+y+" ")
    if choice == "1":
        def nest():
            while True:
                time.sleep(0.3)
                banner()
                choice2 = input(g+"\n    ---["+w+"*"+g+"]"+y+" Encode...\n"+g+"    ---["+w+"1"+g+"]"+y+" ...Texts\n"+g+"    ---["+w+"2"+g+"]"+y+" ...Image\n"+g+"    ---["+w+"3"+g+"]"+y+" Back to menu\n\n"+g+"    ---»»"+y+" ")
                if choice2 == "1" :
                    while True:
                        time.sleep(0.3)
                        banner()
                        choice3 = input(g+"\n    ---["+w+"*"+g+"]"+y+" Means of input:\n"+g+"    ---["+w+"1"+g+"]"+y+" Input Text to encode\n"+g+"    ---["+w+"2"+g+"]"+y+" Select a Text file to encode\n"+g+"    ---["+w+"3"+g+"]"+y+" Back to previous menu\n"+g+"    ---["+w+"4"+g+"]"+y+" Main menu\n\n"+g+"    ---»»"+y+" ")
                        if choice3 == "1":
                            time.sleep(0.3)
                            banner()
                            samp = input(g+"\n---["+w+"•"+g+"]"+y+" Input the text you want to Encode to Base64:\n\n"+g+"--->>"+y+" "+p)
                            banner()
                            time.sleep(0.5)
                            print(g+"\n    ---["+w+"✓"+g+"]"+y+" Successful!")
                            time.sleep(1.0)
                            while True:
                                banner()
                                choice4 = input(g+"\n    ---["+w+"P"+g+"]"+y+" Print result\n"+g+"    ---["+w+"S"+g+"]"+y+" Save as a Txt file\n\n"+g+"    ---»»"+y+" ")
                                if choice4 == "P" or choice4 == "p":
                                    banner()
                                    enc(samp)
                                    break
                                elif choice4 == "S" or choice4 == "s":
                                    banner()
                                    txtEnc(samp)
                                    break
                                else:
                                    time.sleep(0.3)
                                    print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
                                    banner()
                        elif choice3 == "2":
                            def nest2():
                                while True:
                                    try:
                                        banner()
                                        time.sleep(0.3)
                                        file = input(g+"\n---["+w+"?"+g+"]"+y+" Text-file storage path (e.g "+p+"/sdcard/Android/file.txt "+y+") :\n\n"+g+"--->>"+p+" ")
                                        file_open = open(file, 'r')
                                        txtFile = file_open.read()
                                        time.sleep(0.5)
                                        try:
                                            h = txtFile.encode('ascii')
                                            h_encode = base64.b64encode(h)
                                            banner()
                                            print(g+"\n    ---["+w+"✓"+g+"]"+y+" Successful!")
                                            time.sleep(1.0)
                                            while True:
                                                banner()
                                                choice4 = input(g+"\n ---["+w+"P"+g+"]"+y+" Print result\n"+g+"    ---["+w+"S"+g+"]"+y+" Save as a Txt file\n\n"+g+"    ---»»"+y+" ")
                                                if choice4 == "P" or choice4 == "p":
                                                    banner()
                                                    enc(txtFile)
                                                    return
                                                elif choice4 == "S" or choice4 == "s":
                                                    banner()
                                                    txtEnc(txtFile)
                                                    return
                                                else:
                                                    time.sleep(0.3)
                                                    print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
                                                    time.sleep(1.0)
                                        except:
                                            time.sleep(0.3)
                                            print(r+"    ---["+w+"×"+g+"]"+y+" Not a Text-File!")
                                            time.sleep(1.0)
                                            break
                                    except:
                                        time.sleep(0.3)
                                        print(g+"\n    ---["+r+"×"+g+"]"+r+" Text-File Not Found!")
                                        time.sleep(1.0)
                                        break
                            nest2()
                        elif choice3 == "3":
                            time.sleep(0.5)
                            print(g+"\n        ...")
                            time.sleep(0.5)
                            banner()
                            break
                        elif choice3 == "4":
                            time.sleep(0.5)
                            print(g+"\n        ...")
                            time.sleep(0.5)
                            banner()
                            return
                        else:
                            time.sleep(0.3)
                            print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
                            time.sleep(1.0)
                elif choice2 == "2":
                    def nest3():
                        while True:
                            banner()
                            choice5 = input(g+"\n    ---["+w+"*"+g+"]"+y+" Means of input:\n"+g+"    ---["+w+"1"+g+"]"+y+" Select an Image\n"+g+"    ---["+w+"2"+g+"]"+y+" Back to previous menu\n\n"+g+"    ---»»"+y+" ")
                            if choice5 == "1":
                                try:
                                    banner()
                                    time.sleep(0.3)
                                    image = open(input(g+"\n---["+w+"?"+g+"]"+y+" Image-File storage path (e.g "+p+"/sdcard/Android/image.png"+y+"):\n\n"+g+"--->>"+p+" "), 'rb').read()
                                    image_encoded = base64.encodebytes(image)
                                    time.sleep(0.5)
                                    banner()
                                    print(g+"\n    ---["+w+"✓"+g+"]"+y+" Successful!")
                                    time.sleep(1.0)
                                    while True:
                                        banner()
                                        time.sleep(0.3)
                                        choice6 = input(g+"\n    ---["+w+"P"+g+"]"+y+" Print result\n"+g+"    ---["+w+"S"+g+"]"+y+" Save as a Txt file\n("+g+"NOTE: "+y+"Save as text-file instead because image base64 text are large and sophisticated at times): \n\n"+g+"    ---»»"+y+"  ")
                                        if choice6 == "P" or choice6 == "p":
                                            banner()
                                            time.sleep(0.5)
                                            print (y+"\n["+p,image_encoded,y+"]")
                                            input(g+"\n["+y+"ENTER"+g+"]")
                                            return
                                            
                                        elif choice6 == "S" or choice6 == "s":
                                            banner()
                                            saveEncImage(image_encoded)
                                            return
                                        else:
                                            time.sleep(0.3)
                                            print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
                                            time.sleep(1.0)
                                except:
                                    time.sleep(0.3)
                                    print(g+"\n    ---["+r+"×"+g+"]"+r+" Image-File Not Found!")
                                    time.sleep(1.0)
                                    break
                            elif choice5 == "2":
                                time.sleep(0.5)
                                print(g+"\n        ...")
                                time.sleep(0.5)
                                banner()
                                return
                            else:
                                time.sleep(0.3)
                                print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
                                time.sleep(1.0)
                    nest3()     
                elif choice2 == "3":
                    time.sleep(0.5)
                    print(g+"\n        ...")
                    time.sleep(0.5)
                    banner()
                    break
                else:
                    time.sleep(0.3)
                    print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
                    time.sleep(1.0)
        nest()
    elif choice == "2":
        def nest4():
            while True:
                banner()
                time.sleep(0.3)
                choice7 = input(g+"\n    ---["+w+"*"+g+"]"+y+" Decode...\n"+g+"    ---["+w+"1"+g+"]"+y+" ...Texts\n"+g+"    ---["+w+"2"+g+"]"+y+" ...Image\n"+g+"    ---["+w+"3"+g+"]"+y+" Back to menu\n\n"+g+"    ---»»"+y+" ")
                if choice7 == "1" :
                    while True:
                        banner()
                        time.sleep(0.3)
                        choice8 = input(g+"\n    ---["+w+"*"+g+"]"+y+" Means of input:\n"+g+"    ---["+w+"1"+g+"]"+y+" Input Text to decode\n"+g+"    ---["+w+"2"+g+"]"+y+" Select a Text file to decode\n"+g+"    ---["+w+"3"+g+"]"+y+" Back to previous menu\n"+g+"    ---["+w+"4"+g+"]"+y+" Main menu\n\n"+g+"    ---»»"+y+" ")
                        if choice8 == "1":
                            try:
                                banner()
                                time.sleep(0.3)
                                free = input(g+"\n---["+w+"?"+g+"]"+y+" Input the text you want to Decode from Base64 to normal text:\n\n"+g+"--->>"+y+" ")
                                free_byte = free.encode('ascii')
                                base64.b64decode(free_byte)
                                banner()
                                time.sleep(0.5)
                                print(g+"\n    ---["+w+"✓"+g+"]"+y+" Successful!")
                                time.sleep(1.0)
                                while True:
                                    banner()
                                    choice9 = input(g+"\n    ---["+w+"P"+g+"]"+y+" Print result\n"+g+"    ---["+w+"S"+g+"]"+y+" Save as a Txt file\n\n"+g+"    ---»»"+y+" ")
                                    if choice9 == "P" or choice9 == "p":
                                        banner()
                                        dec(free)
                                        break
                                    elif choice9 == "S" or choice9 == "s":
                                        banner()
                                        txtDec(free)
                                        break
                                    else:
                                        time.sleep(0.3)
                                        print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
                                        time.sleep(1.0)
                            except:
                                time.sleep(0.3)
                                print(g+"\n    ---["+r+"×"+g+"]"+r+" Not an encoded base64 Text!")
                                time.sleep(1.0)
                                break
                        elif choice8 == "2":
                            def nest5():
                                while True:
                                    try:
                                        banner()
                                        time.sleep(0.3)
                                        fileX = open(input(g+"\n---[?] Text-file storage path (e.g /sdcard/Android/file.txt ) :\n--->>"), 'r').read()
                                        try:
                                            banner()
                                            txtX_byte = fileX.encode('ascii')
                                            base64.b64decode(txtX_byte)
                                            banner()
                                            time.sleep(0.5)
                                            print(g+"\n    ---["+w+"✓"+g+"]"+y+" Successful!")
                                            time.sleep(1.0)
                                            while True:
                                                banner()
                                                time.sleep(0.3)
                                                choice9 = input(g+"\n    ---["+w+"P"+g+"]"+y+" Print result\n"+g+"    ---["+w+"S"+g+"]"+y+" Save as a Txt file\n\n"+g+"    ---»»"+y+" ")
                                                if choice9 == "P" or choice9 == "p":
                                                    banner()
                                                    dec(fileX)
                                                    return
                                                elif choice9 == "S" or choice9 == "s":
                                                    banner()
                                                    txtDec(fileX)
                                                    return
                                                else:
                                                    time.sleep(0.3)
                                                    print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
                                                    time.sleep(1.0)
                                        except:
                                            time.sleep(0.3)
                                            print(g+"\n    ---["+r+"×"+g+"]"+r+" Not a Base64 Decoded text-file")
                                            time.sleep(1.0)
                                            break
                                    except:
                                        time.sleep(0.3)
                                        print(g+"\n    ---["+r+"×"+g+"]"+r+" Text-File Not Found!")
                                        time.sleep(1.0)
                                        break
                            nest5()
                        elif choice8 == "3":
                            time.sleep(0.5)
                            print(g+"\n        ...")
                            time.sleep(0.5)
                            banner()
                            break
                        elif choice8 == "4":
                            time.sleep(0.5)
                            print(g+"\n        ...")
                            time.sleep(0.5)
                            banner()
                            return
                        else:
                            time.sleep(0.3)
                            print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
                            time.sleep(1.0)
                elif choice7 == "2":
                    def nest6():
                        while True:
                            banner()
                            time.sleep(0.3)
                            choice10 = input(g+"\n    ---["+w+"*"+g+"]"+y+" Means of input:\n"+g+"    ---["+w+"1"+g+"]"+y+" Select an Image encoded in a Text-file to Decode\n"+g+"    ---["+w+"2"+g+"]"+y+" Back to previous menu\n\n"+g+"    ---»»"+y+" ")
                            if choice10 == "1":
                                try:
                                    banner()
                                    time.sleep(0.3)
                                    imageTxt = open(input(g+"\n---["+w+"?"+g+"]"+y+" Image-text_File storage path (e.g "+p+"/sdcard/Android/image.txt):\n\n"+g+">>"+p+" "), 'rb').read()
                                    try:
                                        imageTxt_decoded = base64.urlsafe_b64decode(imageTxt)
                                        banner()
                                        time.sleep(0.5)
                                        print(g+"\n    ---["+w+"✓"+g+"]"+y+" Successful!")
                                        time.sleep(1.0)
                                        banner()
                                        input(g+"\n---["+w+"*"+g+"]"+y+" Saving as an Image file...Press "+g+"[Enter] "+y+"to continue")
                                        banner()
                                        saveDecImage(imageTxt_decoded)
                                        return
                                    except:
                                        time.sleep(0.3)
                                        print(g+"\n    ---["+r+"×"+g+"]"+r+" Not a Base64 Encoded text-file")
                                        time.sleep(1.0)
                                        break
                                except:
                                    time.sleep(0.3)
                                    print(g+"\n    ---["+r+"×"+g+"]"+r+" Image Text-File Not Found!")
                                    time.sleep(1.0)
                                    break
                            elif choice10 == "2":
                                time.sleep(0.5)
                                print(g+"\n        ...")
                                time.sleep(0.5)
                                banner()
                                return
                            else:
                                time.sleep(0.3)
                                print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
                                time.sleep(1.0)
                    nest6()     
                elif choice7 == "3":
                    time.sleep(0.5)
                    print(g+"\n        ...")
                    time.sleep(0.5)
                    banner()
                    break
                else:
                    time.sleep(0.3)
                    print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
                    time.sleep(1.0)
        nest4()
    elif choice == "3":
        os.system("clear")
        print(g+"    ---["+w+"~"+g+"]"+y+" UPDATE STARTED!!!\n"+e)
        time.sleep(0.5)
        os.system("cd $home && rm -rf B64 && apt update -y && apt upgrade -y && apt install python -y && apt install git -y && apt install ruby -y && gem install lolcat && git clone https://github.com/D-MythX/B64 && cd B64 && clear")
        print(g+"\n    ---["+w+"✓"+g+"]"+y+" UPDATE COMPLETED!!!\n")
        time.sleep(1.0)
        print(g+"    ---["+w+"~"+g+"]"+y+" Manually launch tool with \n             [ "+g+"python b64.py"+y+" ]"+e)
        break
    elif choice == "4":
        time.sleep(0.5)
        print(g+"\n        ...")
        time.sleep(0.5)
        banner()
        os.system("figlet Bye! | lolcat")
        print(g+"\n---["+w+"✷"+g+"]"+y+" Credits to Mr. Shell & Abbie"+e)
        break
    else:
        time.sleep(0.3)
        print(g+"\n    ---["+r+"×"+g+"]"+r+" Not In Option!")
        time.sleep(1.0)
        
        
    
   