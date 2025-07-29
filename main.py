with open("prank_log.txt", "a") as f:
    f.write("Prank ran successfully!\n")

import pygame
from PIL import Image
import sys
import os

# ----- Configuration -----
IMAGE_PATH = "image.jpg"  # Replace with your image path
AUDIO_PATH = "sound.mp3"  # Replace with your audio path

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

# Load the image using PIL
try:
    img = Image.open(IMAGE_PATH)
except Exception as e:
    print(f"Failed to open image: {e}")
    sys.exit(1)

# Get screen dimensions
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

# Resize the image to fit the screen
img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)


# Convert the PIL image to a format Pygame understands
mode = img.mode
size = img.size
data = img.tobytes()
image_surface = pygame.image.fromstring(data, size, mode)

# Set up fullscreen display
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Fullscreen Image Viewer")

# Display the image
screen.blit(image_surface, (0, 0))
pygame.display.flip()

# Wait until the music finishes or the user closes the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    if not pygame.mixer.music.get_busy():
        running = False

# Clean up
pygame.quit()
