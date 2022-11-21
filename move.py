# install python
# run the below command in VS Code Terminal
# pip install PyAutoGUI
# run the file by typing the below command 
# python move.py
from email.utils import localtime
import pyautogui
import time
import random

while(1):
    x=random.randint(0,500) # Setting the X-Axis
    y=random.randint(0,500) # Setting the Y-Axis
    pyautogui.moveTo(x,y) #Setting the coordinates

    localtime = time.localtime() # Capture local time for logging
    result = time.strftime("%I:%M:%S %p", localtime) # Format the time to a readable value

    print('Moved at '+ str(result)+ '(' + str(x) + ', '+str(y) + ')') #print out the time in the terminal
    print("Press Ctrl+C to abort/stop the process")
    time.sleep(2) # Do nothing for 2 seconds

#Press Ctrl+C to abort/stop the process