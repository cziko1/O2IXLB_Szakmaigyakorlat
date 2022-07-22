import pyautogui # for the message ... and sending
import time    # for waiting ...

#print('Hello Mate!\nHow can I help you?')

while True:
    time.sleep(2) # it's a waiting time (in second)
    pyautogui.typewrite('Hello Mate!\nHow Can I help you?') #'typewrite' it's a message
    time.sleep(2)
    pyautogui.press('enter') # When I pressed the 'enter' button after this code send a messange.

