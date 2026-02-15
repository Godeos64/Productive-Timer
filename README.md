Break Reminder 👋 

My very first Python project! 

I built this simple script because I spend way too much time staring at my screen. It automatically minimizes all your open windows to force you to take a break, then brings them back so you can get back to work. 
🚀 How It Works 

    The script runs quietly in the background. 
    After a set time, it simulates Win + D to show your desktop. 
    It waits for the break duration to finish. 
    It restores all your windows automatically! 

⚠️ Configuration Note 

The code is currently set to wait 5 seconds for testing purposes. 

To use this for actual breaks, open the script and change time.sleep(5) to time.sleep(1500) (which is 25 minutes). 
🛠️ Installation 

You will need the pynput library to simulate the keyboard inputs: 
bash
 
  
 
pip install pynput
 
 
 
🎮 Usage 

    Run the script:
    bash
     
      
     
    python main.py
     
     
    
    Work as usual! 
    Press the ESC key at any time to stop the program immediately. 

Thanks for checking out my project 
