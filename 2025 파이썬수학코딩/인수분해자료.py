import pygame

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("수식 다이어그램")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 200)

# 폰트 설정
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

# 텍스트 렌더링 함수
def render_text(surface, text, pos, color=BLACK):
    rendered_text = font.render(text, True, color)
    surface.blit(rendered_text, pos)

# 화살표 그리기 함수
def draw_arrow(surface, start, end, color=GREEN):
    pygame.draw.line(surface, color, start, end, width=2)
    arrow_length = 10
    arrow_angle = 30

    # 화살표 머리 계산
    vector = pygame.math.Vector2(end) - pygame.math.Vector2(start)
    angle = vector.angle_to(pygame.math.Vector2(1, 0))
    left_end = pygame.math.Vector2(end) + pygame.math.Vector2(-arrow_length, arrow_length).rotate(angle - arrow_angle)
    right_end = pygame.math.Vector2(end) + pygame.math.Vector2(-arrow_length, -arrow_length).rotate(angle + arrow_angle)

    pygame.draw.polygon(surface, color, [end, left_end, right_end])

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경색 채우기
    screen.fill(YELLOW)

    # 텍스트 추가 (수식 및 값)
    render_text(screen, "3x² + 7x + 2", (200, 50), BLACK)        # 상단 수식
    render_text(screen, "1", (150, 150), BLACK)                 # 좌측 값 "1"
    render_text(screen, "3", (150, 250), BLACK)                 # 좌측 값 "3"
    render_text(screen, "2", (250, 150), BLACK)                 # 중앙 값 "2"
    render_text(screen, "6 ⋯ x + 2", (400, 150), BLACK)         # 우측 상단 결과
    render_text(screen, "1 ⋯ 3x + 1", (400, 250), BLACK)        # 우측 하단 결과
    render_text(screen, "7", (250, 300), BLACK)                 # 하단 결과 "7"

    # 화살표 그리기 (녹색 선)
    draw_arrow(screen, (220, 80), (180, 160), GREEN)            # 위에서 좌측 상단으로 연결
    draw_arrow(screen, (220, 80), (180, 260), GREEN)            # 위에서 좌측 하단으로 연결
    draw_arrow(screen, (180, 160), (240, 160), GREEN)           # 좌측 상단에서 중앙으로 연결
    draw_arrow(screen, (240, 160), (380, 160), GREEN)           # 중앙에서 우측 상단으로 연결
    draw_arrow(screen, (180, 260), (240, 300), GREEN)           # 좌측 하단에서 하단으로 연결
    draw_arrow(screen, (240, 300), (380, 260), GREEN)           # 하단에서 우측 하단으로 연결

    # 화면 업데이트
    pygame.display.flip()

pygame.quit()
