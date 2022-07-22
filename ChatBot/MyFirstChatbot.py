import pyautogui # for the message ... and sending
import time    # for waiting ...

#print('Hello Mate!\nHow can I help you?')

S = 1

while True:
    if S < 5:
        S = S + 2
        time.sleep(S) # it's a waiting time (in second)
        pyautogui.typewrite('Hello Mate!')
        time.sleep(S)
        S = S + 3
        pyautogui.typewrite('\nHow Can I help you?') #'typewrite' it's a message
        pyautogui.press('enter') # When I pressed the 'enter' button after this code send a messange.

    else:
        break

