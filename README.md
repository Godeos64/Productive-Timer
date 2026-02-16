# Productive Timer ⏰

**My very first Python project!**

A simple desktop timer application designed to enforce healthy work habits. It runs in the background and forces you to take breaks by minimizing your windows and displaying notifications, helping prevent eye strain and burnout.

## ✨ What's New?
This version has been updated with a graphical interface (GUI) and a more robust window management system:
*   **GUI Notifications:** Replaces simple print statements with popup windows using PyQt6.
*   **Dark Mode:** Includes a sleek dark mode theme by default.
*   **Updated Shortcuts:** Now uses `Win + M` to minimize and `Shift + Win + M` to restore, which is more reliable than the previous `Win + D` toggle.
*   **Realistic Defaults:** The test timer has been replaced with a standard Pomodoro cycle (25-minute work / 5-minute break).

## 🚀 How it Works

1.  Run the script to start your work session.
2.  Work for **25 minutes**.
3.  The script minimizes all your windows automatically.
4.  A popup appears notifying you: **"Take a break!"**
5.  After **5 minutes**, a second popup alerts you: **"Let's get back to work!"**
6.  The script restores all your windows automatically, so you can get back to it.

## 🛠️ Installation

You will need `pynput` for keyboard controls and `PyQt6` for the graphical popups.

```
pip install pynput PyQt6
```

## 🎮 Usage

Run the main script in your terminal:

```
python Main.py
```

To stop the program at any time, press the **ESC** key.

## ⚙️ Configuration

### Adjusting Times
The timer is set to a standard 25/5 split by default. To change this, open `Main.py` and modify the `time.sleep()` values (in seconds):

*   **Work Time:** `time.sleep(1500)` (Currently 25 mins)
*   **Break Time:** `time.sleep(300)` (Currently 5 mins)

### Switching Themes
The app defaults to **Dark Mode**. If you prefer a native system look (Light Mode):

1.  Open `Main.py`.
2.  Locate the import line at the top:
    ```
    from GUI_Dark_mode import MessageBox
    ```
3.  Change it to:
    ```
    from GUI_Light_mode import MessageBox
    ```

---

Thanks for checking out my project!
