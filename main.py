import subprocess
import os
import sys

IMAGE_PATH = "image.jpg"
AUDIO_PATH = "sound.mp3"

# Write log
with open("prank_log.txt", "a") as f:
    f.write("Prank ran successfully!\n")

# Play audio
try:
    subprocess.Popen(["ffplay", "-nodisp", "-autoexit", AUDIO_PATH])
except Exception as e:
    print("Audio failed:", e)

# Show image in ffplay
try:
    subprocess.Popen(["ffplay", "-loop", "1", IMAGE_PATH])
except Exception as e:
    print("Image failed:", e)
