from PIL import Image
import pygame
import sys

pygame.init()

screen=pygame.display.set_mode((1000,500))
clock=pygame.time.Clock()
running=True
try:
  image=pygame.image.load("frame_1.png")
except pygame.error as e:
    print(f"Error loading image:{e}")
    sys.exit(1)
 
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((255,255,255))
    screen.blit(image,(0,0))

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
