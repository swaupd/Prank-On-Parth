from moviepy.editor import VideoFileClip
import pygame
import sys

VIDEO_PATH = "prank.mp4"

# Log
with open("prank_log.txt", "a") as f:
    f.write("Prank video launched.\n")

# Load video
clip = VideoFileClip(VIDEO_PATH)
video_size = clip.size  # (width, height)
fps = clip.fps

# Init pygame
pygame.init()
screen = pygame.display.set_mode(video_size, pygame.FULLSCREEN)
pygame.display.set_caption("Prank Video")

# Play video frame by frame
clock = pygame.time.Clock()

for frame in clip.iter_frames(fps=fps, dtype="uint8"):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit(0)

    surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
    screen.blit(surface, (0, 0))
    pygame.display.update()
    clock.tick(fps)

# Cleanup
pygame.quit()
