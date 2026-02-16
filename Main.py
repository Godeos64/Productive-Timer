import time
from os import _exit
from pynput import keyboard
from pynput.keyboard import Key
from PyQt6.QtWidgets import QApplication, QMessageBox
from GUI_Dark_mode import MessageBox
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

def minimize_windows(): 
    # Minimizes all windows using Win + M
    Controller.press(Key.cmd)
    Controller.press("m")
    Controller.release("m")
    Controller.release(Key.cmd)

def restore_windows():
     # Restores minimized windows using Shift + Win + M
    Controller.press(Key.cmd)
    Controller.press(Key.shift)
    Controller.press("m")
    Controller.release("m")
    Controller.release(Key.shift)
    Controller.release(Key.cmd)

# Main

while Active:
     time.sleep(5) # waits 25 minutes
     minimize_windows() # minimizes all windows
     MessageBox("Take a break!", "Break Time")
     

     time.sleep(3) # waits 5 minutes 
     MessageBox("Let's get back to work!", "Break Over")
     restore_windows() # restores windows  
