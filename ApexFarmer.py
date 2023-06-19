from pyautogui import *
import pyautogui
import time
import keyboard
import random

#import win32api, win32con
import numpy as np

Random = ['a','w','s','d','4','q','1','2','3','4']

time.sleep(2)

# check if the P key is being pressed (if pressed it will pause the execution of below loop)
# while keyboard.is_pressed('p') == False:

while True:
    
    # Disable Fill Teammates
    if pyautogui.locateOnScreen('Team.png', region=(3,520,445,304), grayscale=True, confidence=0.9) != None:
        pyautogui.click(171, 675)
        time.sleep(np.random.uniform(0.3,0.7))
        pyautogui.click(171, 675)
        time.sleep(np.random.uniform(0.5,1.2))

    # Ready Matchmaking
    if pyautogui.locateOnScreen('ManuNotReady.png', region=(0,538,447,528), grayscale=True, confidence=0.7) != None:
        pyautogui.click(230, 950)
        time.sleep(np.random.uniform(0.3,0.8))
        pyautogui.click(230, 950)     
        time.sleep(np.random.uniform(0.3,0.75))
        pyautogui.click(230, 950)
        time.sleep(np.random.uniform(0.5,1.1))
        
    if pyautogui.locateOnScreen('InGame.png', region=(87, 755, 379, 304), grayscale=True, confidence=0.5) is not None:
        print("In game waiting")
        keyboard.press_and_release(Random)
        time.sleep(0.5)
        if '4' in Random:
            time.sleep(np.random.uniform(5.5,6))
        else:
            time.sleep(np.random.uniform(0.6, 1.5)) 
    
    if pyautogui.locateOnScreen('dead.png', region=(441,19,1017,304), grayscale=True, confidence=0.6) != None:
        print("dead")
        pyautogui.press('space')
        time.sleep(np.random.uniform(0.2,0.4))
                
        
    if pyautogui.locateOnScreen('leave.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
        pyautogui.click(963, 623)
        time.sleep(np.random.uniform(0.4,0.8))
        pyautogui.press('esc')
     
    if pyautogui.locateOnScreen('space.png', region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
        keyboard.press_and_release('space')
        time.sleep(np.random.uniform(0.2,0.4))
     
    if pyautogui.locateOnScreen('yes.png', region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
        pyautogui.click(850, 713)
        time.sleep(np.random.uniform(0.4,0.8))
        pyautogui.click(850, 713)
         
    if pyautogui.locateOnScreen('Contunue.png', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
        pyautogui.click(952, 717)
        time.sleep(np.random.uniform(0.4,0.7))
        pyautogui.click(952, 717)
         
    if pyautogui.locateOnScreen('startmanu.png', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
        pyautogui.click(952, 717)
        time.sleep(np.random.uniform(0.4,0.8))
        pyautogui.click(952, 717)
    
    if pyautogui.locateOnScreen('startmanu.png', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
        pyautogui.click(952, 717)
        time.sleep(np.random.uniform(0.3,0.7))
        pyautogui.click(952, 717)
