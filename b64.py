#!/usr/bin/env python3
#Title: Base64 encoder & decoder
#Author: MY7H

import os
import base64
import time

y = "\033[2;33m"
g = "\033[2;32m"
p = "\033[2;35m"
w = "\033[2;37m"
r = "\033[2;31m"
e = "\033[0m"
u = "\033[4m"
B = "\033[2;01m"

def enc(text):
    text_byte = text.encode('ascii')
    text_encode = base64.b64encode(text_byte) 
    text_b64 = text_encode.decode('ascii')
    print(g+"\n["+w+"✓"+g+"]"+y+" Encoded to:["+p,text_b64,y+"]")
    
def txtEnc(text):
    text_byte = text.encode('ascii')
    text_encode = base64.b64encode(text_byte) 
    text_b64 = text_encode.decode('ascii')
    x = input(g+"\n["+w+"?"+g+"]"+y+" What would you want to be the title of your Text_File? "+g+"")
    file = open("/sdcard/Android/"+x+"Enc.txt", 'w')
    file.write(text_b64)
    file.close()
    print(g+"\n"+g+"["+w+"✓"+g+"]"+y+" Saved to: "+g+"Storage"+y+" >> "+g+"Android "+w+">>"+g+" "+x+"Enc.txt")

def saveEncImage(text):
    x = input(g+"\n["+w+"?"+g+"]"+y+" What would you want to be the title of your Image_txtFile? "+g+"")
    file = open("/sdcard/Android/"+x+"Enc.txt", 'wb')
    file.write(text)
    file.close()
    print(g+"\n["+w+"✓"+g+"]"+y+" Saved to: "+g+"Storage "+y+">> "+g+"Android "+y+">>"+g+" "+x+"Enc.txt")

def dec(text):
    text_byte = text.encode('ascii')
    text_encode = base64.b64decode(text_byte) 
    text_b64 = text_encode.decode('ascii')
    print(g+"\n["+w+"✓"+g+"]"+y+" Decoded to:["+p,text_b64,y+"]")
    
def txtDec(text):
    text_byte = text.encode('ascii')
    text_encode = base64.b64decode(text_byte) 
    text_b64 = text_encode.decode('ascii')
    x = input(g+"\n["+w+"?"+g+"]"+y+" What would you want to be the title of your Text_File? "+g+"")
    file = open("/sdcard/Android/"+x+"Dec.txt", 'w')
    file.write(text_b64)
    file.close()
    print(g+"\n["+w+"✓"+g+"] "+y+"Saved to: "+g+"Storage "+y+">> "+g+"Android "+y+">>"+g+" "+x+"Dec.txt")

def saveDecImage(text):
    x = input(g+"\n["+w+"?"+g+"] "+y+"What would you want to be the title of your Decoded Image?"+g+" ")
    file = open("/sdcard/Android/"+x+"Dec.jpg", 'wb')
    file.write(text)
    file.close()
    print(g+"\n["+w+"✓"+g+"]"+y+" Saved to: "+g+"Storage "+y+">>"+g+" Android "+y+">>"+g+" "+x+"Dec.jpg") 
    
os.system("figlet Base64 | lolcat")
time.sleep(1.0)
print(p+"Encoder and Decoder for Texts and Images")
time.sleep(1.0)
print('Author:  “ '+r+'MY7H'+p+' ” '+e)
while True:
    choice = input(g+"\n["+w+"*"+g+"]"+y+" Pick Option:\n"+g+"["+w+"1"+g+"]"+y+" Encode\n"+g+"["+w+"2"+g+"]"+y+" Decode\n"+g+"["+w+"3"+g+"]"+y+" Update tool\n"+g+"["+w+"4"+g+"]"+r+" Exit\n\n"+g+"»»"+y+" ")
    if choice == "1":
        def nest():
            while True:
                choice2 = input(g+"\n["+w+"*"+g+"]"+y+" Encode...\n"+g+"["+w+"1"+g+"]"+y+" ...Texts\n"+g+"["+w+"2"+g+"]"+y+" ...Image\n"+g+"["+w+"3"+g+"]"+y+" Back to menu\n\n"+g+"»»"+y+" ")
                if choice2 == "1" :
                    while True:
                        choice3 = input(g+"\n["+w+"*"+g+"]"+y+" Means of input:\n"+g+"["+w+"1"+g+"]"+y+" Input Text to encode\n"+g+"["+w+"2"+g+"]"+y+" Select a Text file to encode\n"+g+"["+w+"3"+g+"]"+y+" Back to previous menu\n"+g+"["+w+"4"+g+"]"+y+" Main menu\n\n"+g+"»»"+y+" ")
                        if choice3 == "1":
                            samp = input(g+"\n["+w+"•"+g+"]"+y+" Input the text you want to Encode to Base64:\n\n"+g+">>"+y+" "+p)
                            print(g+"\n["+w+"*"+g+"]"+y+" Successful!")
                            while True:
                                choice4 = input(g+"\n["+w+"P"+g+"]"+y+" Print result\n"+g+"["+w+"S"+g+"]"+y+" Save as a Txt file\n\n"+g+"»»"+y+" ")
                                if choice4 == "P" or choice4 == "p":
                                    enc(samp)
                                    break
                                elif choice4 == "S" or choice4 == "s":
                                    txtEnc(samp)
                                    break
                        elif choice3 == "2":
                            def nest2():
                                while True:
                                    try:
                                        file = input(g+"\n["+w+"?"+g+"]"+y+" Text-file storage location (e.g "+p+"/sdcard/Android/file.txt "+y+") :\n\n"+g+">>"+p+" ")
                                        file_open = open(file, 'r')
                                        txtFile = file_open.read()
                                        print(g+"\n["+w+"✓"+g+"]"+y+" Successful!")
                                        while True:
                                            choice4 = input(g+"\n["+w+"P"+g+"]"+y+" Print result\n"+g+"["+w+"S"+g+"]"+y+" Save as a Txt file")
                                            if choice4 == "P" or choice4 == "p":
                                                enc(txtFile)
                                                return
                                            elif choice4 == "S" or choice4 == "s":
                                                txtEnc(txtFile)
                                                return
                                    except:
                                        print(g+"\n["+r+"×"+g+"]"+r+" Text-File Not Found!")
                            nest2()
                        elif choice3 == "3":
                            print(g+"\n...")
                            break
                        elif choice3 == "4":
                            print(g+"\n...")
                            return
                        else:
                            print(g+"\n["+r+"×"+g+"]"+r+" Not In Option!")
                elif choice2 == "2":
                    def nest3():
                        while True:
                            choice5 = input(g+"\n["+w+"*"+g+"]"+y+" Means of input:\n"+g+"["+w+"1"+g+"]"+y+" Select an Image\n"+g+"["+w+"2"+g+"]"+y+" Back to previous menu\n\n"+g+"»»"+y+" ")
                            if choice5 == "1":
                                try:
                                    image = open(input(g+"\n["+w+"?"+g+"]"+y+" Image-File storage location (e.g "+p+"/sdcard/Android/image.png"+y+"):\n\n"+g+">>"+p+" "), 'rb')
                                    image_read = image.read()
                                    image_encoded = base64.encodebytes(image_read)
                                    print(g+"["+w+"✓"+g+"]"+y+" Successful!")
                                    while True:
                                        choice6 = input(g+"\n["+w+"P"+g+"]"+y+" Print result\n"+g+"["+w+"S"+g+"]"+y+" Save as a Txt file\n("+g+"NOTE: "+y+"Save as text-file instead because image base64 text are large and sophisticated at times): \n\n"+g+"»»"+y+"  ")
                                        if choice6 == "P" or choice6 == "p":
                                            print (y+"\n["+p,image_encoded,y+"]")
                                            return
                                            
                                        elif choice6 == "S" or choice6 == "s":
                                            saveEncImage(image_encoded)
                                            return
                                        else:
                                            print(g+"\n["+r+"×"+g+"]"+r+" Not In Option!")
                                except:
                                    print(g+"\n["+r+"×"+g+"]"+r+" Image-File Not Found!")
                            elif choice5 == "2":
                                return
                            else:
                                print(g+"\n["+r+"×"+g+"]"+r+" Not In Option!")
                    nest3()     
                elif choice2 == "3":
                    break
                else:
                    print(g+"\n["+r+"×"+g+"]"+r+" Not In Option!")
        nest()
    elif choice == "2":
        def nest4():
            while True:
                choice7 = input(g+"\n["+w+"*"+g+"]"+y+" Decode...\n"+g+"["+w+"1"+g+"]"+y+" ...Texts\n"+g+"["+w+"2"+g+"]"+y+" ...Image\n"+g+"["+w+"3"+g+"]"+y+" Back to menu\n\n"+g+"»»"+y+" ")
                if choice7 == "1" :
                    while True:
                        choice8 = input(g+"\n["+w+"*"+g+"]"+y+" Means of input:\n"+g+"["+w+"1"+g+"]"+y+" Input Text to decode\n"+g+"["+w+"2"+g+"]"+y+" Select a Text file to decode\n"+g+"["+w+"3"+g+"]"+y+" Back to previous menu\n"+g+"["+w+"4"+g+"]"+y+" Main menu\n\n"+g+"»»"+y+" ")
                        if choice8 == "1":
                            try:
                                free = input(g+"\n["+w+"?"+g+"]"+y+" Input the text you want to Decode from Base64 to normal text:\n\n"+g+">>"+y+" ")
                                free_byte = free.encode('ascii')
                                base64.b64decode(free_byte)
                                print(g+"["+w+"✓"+g+"]"+y+" Successful!")
                                while True:
                                    choice9 = input(g+"\n["+w+"P"+g+"]"+y+" Print result\n"+g+"["+w+"S"+g+"]"+y+" Save as a Txt file\n\n"+g+"»»"+y+" ")
                                    if choice9 == "P" or choice9 == "p":
                                        dec(free)
                                        break
                                    elif choice9 == "S" or choice9 == "s":
                                        txtDec(free)
                                        break
                            except:
                                print(g+"\n["+r+"×"+g+"]"+r+" Not an encoded base64 Text!")
                        elif choice8 == "2":
                            def nest5():
                                while True:
                                    try:
                                        fileX = open(input(g+"\n[?] Text-file storage location (e.g /sdcard/Android/file.txt ) :\n"), 'r')
                                        txtFileX = fileX.read()
                                        try:
                                            txtX_byte = txtFileX.encode('ascii')
                                            base64.b64decode(txtX_byte)
                                            print(g+"\n["+w+"✓"+g+"]"+y+" Successful!")
                                            while True:
                                                choice9 = input(g+"\n["+w+"P"+g+"]"+y+" Print result\n"+g+"["+w+"S"+g+"]"+y+" Save as a Txt file\n\n"+g+"»»"+y+" ")
                                                if choice9 == "P" or choice9 == "p":
                                                    dec(txtFileX)
                                                    return
                                                elif choice9 == "S" or choice9 == "s":
                                                    txtDec(txtFileX)
                                                    return
                                        except:
                                            print(g+"\n["+r+"×"+g+"]"+r+" Not a Base64 Decoded text-file")
                                            break
                                    except:
                                        print(g+"\n["+r+"×"+g+"]"+r+" Text-File Not Found!")
                                        break
                            nest5()
                        elif choice8 == "3":
                            print(g+"\n...")
                            break
                        elif choice8 == "4":
                            print("g+\n...")
                            return
                        else:
                            print(g+"\n["+r+"×"+g+"]"+r+" Not In Option!")
                elif choice7 == "2":
                    def nest6():
                        while True:
                            choice10 = input(g+"\n["+w+"*"+g+"]"+y+" Means of input:\n"+g+"["+w+"1"+g+"]"+y+" Select an Image encoded in a Text-file to Decode\n"+g+"["+w+"2"+g+"]"+y+" Back to previous menu\n\n"+g+"»»"+y+" ")
                            if choice10 == "1":
                                try:
                                    imageTxt = open(input(g+"\n["+w+"?"+g+"]"+y+" Image-text_File storage location (e.g "+p+"/sdcard/Android/image.txt):\n\n"+g+">>"+p+" "), 'r')
                                    imageTxt_read = imageTxt.read()
                                    try:
                                        imageTxt_decoded = base64.decodebytes(imageTxt_read)
                                        print(g+"\n["+w+"✓"+g+"]"+y+" Successful!")
                                        input(g+"\n["+w+"*"+g+"]"+y+" Saving as an Image file...Press "+g+"[Enter] "+y+"to continue")
                                        saveDecImage(imageTxt_decoded)
                                        return
                                    except:
                                        print(g+"\n["+r+"×"+g+"]"+r+" Not a Base64 Encoded text-file")
                                except:
                                    print(g+"\n["+r+"×"+g+"]"+r+" Image Text-File Not Found!")
                            elif choice10 == "2":
                                return
                            else:
                                print(g+"\n["+r+"×"+g+"]"+r+" Not In Option!")
                    nest6()     
                elif choice7 == "3":
                    break
                else:
                    print(g+"\n["+r+"×"+g+"]"+r+" Not In Option!")
        nest4()
    elif choice == "3":
        os.system("clear")
        os.system("cd $home")
        os.system("rm -rf B64")
        os.system("apt update")
        os.system("apt upgrade -y")
        os.system("apt install python -y")
        os.system("apt install figlet -y")
        os.system("apt install git -y")
        os.system("apt install ruby -y")
        os.system("gem install lolcat")
        os.system("git clone https://github.com/D-MythX/B64 ")
        os.system("cd B64")
        os.system("clear")
        print(g+"["+w+"✓"+g+"]"+y+" UPDATE COMPLETED!!!\n")
        time.sleep(1.0)
        print(g+"["+w+"~"+g+"]"+y+" LAUNCHING TOOL IN 5secs..."+e)
        time.sleep(5.0)
        os.system("b64.py")
    elif choice == "4":
        os.system("figlet *Bye* | lolcat")
        print("Credits to AnonyimHack5 & Abbie")
        break
    else:
        print("\nNot In Option!")
        
        
         #        /sdcard/Android/testEnc.txt