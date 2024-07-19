from PIL import Image, ImageTk
import pystray
import tkinter as tk
from tkinter import messagebox
import threading
import time

# Global variables
timer_thread = None
running = False
paused = False
remaining_time = 0

def start_timer(duration):
    global running, paused, remaining_time
    running = True
    paused = False
    remaining_time = duration * 60
    while running and remaining_time > 0:
        if not paused:
            time.sleep(1)
            remaining_time -= 1
            update_time_display()
        else:
            time.sleep(1)
    if remaining_time <= 0:
        show_message("Time's up!")
    running = False

def update_time_display():
    global remaining_time
    mins, secs = divmod(remaining_time, 60)
    time_string = f"{mins:02d}:{secs:02d}"
    time_label.config(text=time_string)

def start_work_session():
    global timer_thread
    if timer_thread and timer_thread.is_alive():
        stop_timer()
    timer_thread = threading.Thread(target=start_timer, args=(25,))
    timer_thread.start()

def start_break_session():
    global timer_thread
    if timer_thread and timer_thread.is_alive():
        stop_timer()
    timer_thread = threading.Thread(target=start_timer, args=(5,))
    timer_thread.start()

def stop_timer():
    global running, paused
    running = False
    paused = False
    update_time_display()

def pause_timer():
    global paused
    paused = not paused
    if paused:
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")

def reset_timer():
    global running, paused
    if running:
        stop_timer()
    update_time_display()
    start_work_session()

def show_message(message):
    messagebox.showinfo("Pomodoro Timer", message)

def on_quit(icon, item):
    icon.stop()
    root.destroy()

def setup_system_tray():
    icon = pystray.Icon("test_icon")
    icon.icon = Image.open("icon.png")
    icon.menu = pystray.Menu(
        pystray.MenuItem("Start Work Session", lambda: start_work_session()),
        pystray.MenuItem("Start Break Session", lambda: start_break_session()),
        pystray.MenuItem("Quit", on_quit)
    )
    icon.run()

# Tkinter setup
root = tk.Tk()
root.title("Pomodoro Timer")

# GUI components
time_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
time_label.pack(pady=20)

start_button = tk.Button(root, text="Start", command=start_work_session)
start_button.pack(side=tk.LEFT, padx=10)

pause_button = tk.Button(root, text="Pause", command=pause_timer)
pause_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(root, text="Reset", command=reset_timer)
reset_button.pack(side=tk.LEFT, padx=10)

# Start system tray icon
tray_thread = threading.Thread(target=setup_system_tray, daemon=True)
tray_thread.start()

root.mainloop()