import pyautogui # for the message ... and sending
import time    # for waiting ...

#print('Hello Mate!\nHow can I help you?')

S = 0

while True:
    if S < 5:  # If the waiting time is bigger than 5s.
        S = S + 2 # The value of the waiting time
        time.sleep(S) # it's a waiting time (in second)
        pyautogui.typewrite('Hello Mate!')
        S = S + 3
        time.sleep(S)
        pyautogui.typewrite('\nHow Can I help you?') #'typewrite' it's a message
        pyautogui.press('enter') # When I pressed the 'enter' button after this code send a messange.

    else:
        break   # exit the loop
