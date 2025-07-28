import pygame
from PIL import Image
import os
import sys

# ----- Log Start -----
try:
    with open("prank_log.txt", "a") as f:
        f.write("Prank ran successfully!\n")
except Exception as log_err:
    print(f"Log write failed: {log_err}")

# ----- Configuration -----
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(SCRIPT_DIR, "image.jpg")   # Replace with actual filename if different
AUDIO_PATH = os.path.join(SCRIPT_DIR, "sound.mp3")   # Replace with actual filename if different

# ----- Initialize Pygame -----
pygame.init()
pygame.mixer.init()

# Load and play audio
try:
    pygame.mixer.music.load(AUDIO_PATH)
    pygame.mixer.music.play()
except Exception as e:
    print(f"Failed to play audio: {e}")
    sys.exit(1)

# Load image using PIL
try:
    img = Image.open(IMAGE_PATH)
except Exception as e:
    print(f"Failed to open image: {e}")
    sys.exit(1)

# Get screen size
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

# Resize image to screen size
img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
mode = img.mode
size = img.size
data = img.tobytes()

# Convert PIL image to Pygame surface
image_surface = pygame.image.fromstring(data, size, mode)

# Display full screen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("You Got Pranked!")

screen.blit(image_surface, (0, 0))
pygame.display.flip()

# Wait for music to end or user input
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    if not pygame.mixer.music.get_busy():
        running = False

pygame.quit()
