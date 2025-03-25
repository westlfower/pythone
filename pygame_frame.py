import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 이미지 로드
image = pygame.Surface((100, 100))
image.fill((255, 0, 0))  # 빨간색 사각형

# 초기 위치, 각도, 크기 설정
x, y = screen_width // 2, screen_height // 2
angle = 0
scale = 1

# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                scale *= 1.2
            elif event.key == pygame.K_DOWN:
                scale /= 1.2
            elif event.key == pygame.K_LEFT:
                angle -= 15
            elif event.key == pygame.K_RIGHT:
                angle += 15

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 5
    if keys[pygame.K_s]:
        y += 5
    if keys[pygame.K_a]:
        x -= 5
    if keys[pygame.K_d]:
        x += 5

    # 이미지 회전 및 확대
    rotated_image = pygame.transform.rotozoom(image, angle, scale)

    # 화면 채우기
    screen.fill((0, 0, 0))

    # 회전된 이미지를 화면에 그리기
    rect = rotated_image.get_rect(center=(x, y))
    screen.blit(rotated_image, rect)

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 제한
    pygame.time.Clock().tick(60)
