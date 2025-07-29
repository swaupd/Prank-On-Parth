import subprocess
import os

video_path = os.path.abspath("jumpscare.mp4")

# Launch ffplay in fullscreen, no controls or window decorations
subprocess.Popen([
    subprocess.Popen(["ffplay", "-fs", "-noborder", "-autoexit", video_path])
])
