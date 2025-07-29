import tkinter as tk
import subprocess
import os

# Path to the video
video_path = os.path.abspath("jumpscare.mp4")

# Create a Tkinter window to detect screen info
root = tk.Tk()
root.withdraw()  # Hide the root window

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Suppose second monitor starts at x=1920
# (you can dynamically detect this if needed via libraries like `screeninfo`)
second_monitor_x = 1920
second_monitor_y = 0

# Launch ffplay on the second monitor
subprocess.Popen([
    "ffplay",
    "-fs",           # Fullscreen
    "-noborder",     # Remove window borders
    "-x", str(screen_width),
    "-y", str(screen_height),
    "-left", str(second_monitor_x),
    "-top", str(second_monitor_y),
    "-autoexit",
    "-loglevel", "quiet",
    video_path
])
