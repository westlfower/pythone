import pygame
import random
import re

# 초기 설정
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("인수분해 마스터")
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (30,144,255)
RED = (255,0,0)
GREEN = (0,255,0)
GRAY = (200,200,200)

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, text):
        super().__init__()
        self.image = pygame.Surface((100,50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.original_pos = (x,y)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.dragging = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        text_surface = self.font.render(self.text, True, WHITE)
        surface.blit(text_surface, (self.rect.x+10, self.rect.y+10))

def generate_problem():
    a = random.choice([1,2])
    b = random.randint(1,5)
    c = random.choice([1,2])
    d = random.randint(1,5)
    
    problem = f"{(a*c)}x² + {(a*d + b*c)}x + {b*d}"
    blocks = [
        f"{a}x" if a !=1 else "x",
        str(b),
        f"{c}x" if c !=1 else "x",
        str(d)
    ]
    random.shuffle(blocks)
    return problem, blocks

def parse_term(text):
    if 'x' in text:
        return (int(text.replace('x','')) if text != 'x' else 1, 0)
    else:
        return (0, int(text))

def check_answer(factor1, factor2, problem):
    a1 = factor1[0][0] + factor1[1][0]
    b1 = factor1[0][1] + factor1[1][1]
    a2 = factor2[0][0] + factor2[1][0]
    b2 = factor2[0][1] + factor2[1][1]
    
    expanded = (
        a1*a2,
        a1*b2 + a2*b1,
        b1*b2
    )
    return expanded == problem

def main():
    problem, solution = generate_problem()
    target_coeffs = list(map(int, re.findall(r'-?\d+', problem)))
    
    font = pygame.font.Font(None, 48)
    blocks = [Block(150*i+50, 450, text) for i, text in enumerate(solution)]
    factor1_zone = pygame.Rect(100, 200, 200, 100)
