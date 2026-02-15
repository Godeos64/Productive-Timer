import time
from os import _exit
from pynput import keyboard
from pynput.keyboard import Key

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

def windows_d():
     Controller.press(Key.cmd)
     Controller.press("d")
     Controller.release(Key.cmd)
     Controller.release("d")

# Main

while Active:
     time.sleep(5) # waits 25 minutes
     windows_d() # minimizes all windows
     print("take a break, boss!") # random motivation

     time.sleep(5) # waits 5 minutes 

     windows_d() # restores windows
     print("let's get back to work.")
     
