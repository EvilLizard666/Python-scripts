import pyautogui
import os
import PySimpleGUI as psg
import time


PlayButton1       =(317, 123)
BlindPick1 	  =(425, 720)
ConfirmButton1 	  =(836, 935)
AcceptMatch1   	  =(959, 767)
PickChamp1        =(900, 654)
LockIn1           =(944, 817)
MoveChamp1        =(32,  876)
PlayButton2       =(118, 167)
BlindPick2 	  =(226, 644)
ConfirmButton2 	  =(541, 816)
AcceptMatch2   	  =(541, 816)
PickChamp2        =(583, 581)
LockIn2           =(640, 736)
pyautogui.PAUSE   =1



def bot_res1():
    pyautogui.moveTo(PlayButton1) 		#Play Button Move
    pyautogui.click()           		#Play click
    pyautogui.moveTo(BlindPick1) 		#Blind Button Move
    pyautogui.click()					#Blind click
    pyautogui.moveTo(ConfirmButton1) 	#Confirm Button Move
    pyautogui.click()					#Confirm click
    pyautogui.moveTo(ConfirmButton1)
    pyautogui.click()					#Find match click
    pyautogui.moveTo(AcceptMatch1) 		#Accept match button
    while True:
        pyautogui.moveTo(AcceptMatch1)
        pyautogui.click()
        pyautogui.moveTo(PickChamp1)
        pyautogui.click()
        pyautogui.moveTo(LockIn1)
        pyautogui.click()               #Clicking
        Detecting_Client  =os.popen('wmic process get description, processid').read()
        if "League of Legends.exe" in Detecting_Client:
            while True:
                Detecting_Client  =os.popen('wmic process get description, processid').read()
                pyautogui.moveTo(1758, 605)
                pyautogui.click()
                pyautogui.moveTo(MoveChamp1)   #Moving Champ
                pyautogui.mouseDown(button = 'right')     #Moving Champ from the map
                pyautogui.mouseUp(button = 'right')
                if "League of Legends.exe" not in Detecting_Client:
                    break
                    while True:
                        pyautogui.moveTo(961, 888)
                        pyautogui.click()
                        pyautogui.moveTo(840, 921)
                        pyautogui.click()
                        pyautogui.moveTo(835, 925)
                        pyautogui.click()
                        
                
def bot_res2():
    pyautogui.moveTo(PlayButton2) 		#Play Button Move
    pyautogui.click()           		#Play click
    pyautogui.moveTo(BlindPick2) 		#Blind Button Move
    pyautogui.click()					#Blind click
    pyautogui.moveTo(ConfirmButton2) 	#Confirm Button Move
    pyautogui.click()					#Confirm click
    pyautogui.moveTo(ConfirmButton2)
    pyautogui.click()					#Find match click
    pyautogui.moveTo(AcceptMatch2) 		#Accept match button
    while True:
        pyautogui.moveTo(AcceptMatch2)
        pyautogui.click()
        pyautogui.moveTo(PickChamp2)
        pyautogui.click()
        pyautogui.moveTo(LockIn2)
        pyautogui.click()               #Clicking
        Detecting_Client  =os.popen('wmic process get description, processid').read()
        while "League of Legends.exe" in Detecting_Client:
            time.sleep(0.5)
            pyautogui.moveTo(MoveChamp1)
            pyautogui.mouseDown(button = 'right')
            pyautogui.mouseUp(button = 'right')
        if "League of Legends.exe" not in Detecting_Client:
            break

#GUI Layout
psg.theme('DarkBlack')
layout = [[psg.Text('Choose Your Monitor Resolution',size = (50, 1), font = 'Lucida',justification = 'left')],
		  [psg.Text('Bot Usage:\n1.Open the Game Client.\n2.Open the Bot program\n3.Choose Your Monitor Resolution.\n4.Click on Start Bot.', font = 'Lucida')],
          [psg.Listbox(values = ['1920x1080','1280x1024'], select_mode ='extended', key ='res', size = (30, 6))],
          [psg.Button('Start Bot', font = ('Lucida',12), key = 'st'),psg.Button('Cancel', font = ('Lucida',12))]]
win = psg.Window('League Bot',layout)
e,v = win.read()

while True:
    if e == psg.WIN_CLOSED or e == 'Cancel':  #If user closes window or clicks cancel
        win.close()
        break
    elif v['res'] == ['1920x1080']:           # If user choose 1920x1080
        bot_res1()
    elif v['res'] == ['1280x1024']:           # If user choose 1280x1024
        bot_res2()

    
