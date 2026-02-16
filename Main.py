import time
from os import _exit
from pynput import keyboard
from pynput.keyboard import Key
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from GUI import MessageBox # choose one of the 2 themes in the GUI files.
# Config

Controller = keyboard.Controller()
Active = True

# function

def on_press(key):  # emergency exit
     global Active 
     try:
          if key == Key.esc: # if escape is pressed, the program will stop
               _exit(0)
     except AttributeError: # if any other key is pressed, it will do nothing
          pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

def windows_d(): # minimizes/restores all windows by pressing Windows + D
     Controller.press(Key.cmd)
     Controller.press("d")
     Controller.release(Key.cmd)
     Controller.release("d")

# Main

while Active:
     time.sleep(5) # waits 25 minutes
     windows_d() # minimizes all windows
     MessageBox("Take a break!", "Break Time").show()
     

     time.sleep(3) # waits 5 minutes 

     windows_d() # restores windows
     MessageBox("Let's get back to work!", "Break Over").show()
     
