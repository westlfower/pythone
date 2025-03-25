import pygame
import sys
from PIL import Image
images=[]

for i in range(10):
    img=Image.open(f'frame_{i+1}.png')
    resized_img=img.resize((200,140))
    resized_img.save(f'frame_resized_{i+1}.png')

for i in range(10):
    image=pygame.image.load(f'frame_resized_{i+1}.png')
    images.append(image)


def main():
    pygame.init()
    screen=pygame.display.set_mode((960,720))
    clock=pygame.time.Clock()
    i=0
        

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255,255,255))
        screen.blit(images[i],[80*i,0])
        i=(i+1)%10
        pygame.display.update()
        clock.tick(3)

if __name__ =='__main__':
    main()
