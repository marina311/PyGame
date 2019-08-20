import pygame
from random import randint


class Ball:
    def __init__(self, pos):
        self.pos = pos
        self.color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.size = randint(5, 30)

    def update(self, d):
        if self.pos[1] <= YMAX - self.size:
            self.pos = (self.pos[0], self.pos[1] + d)
        pygame.draw.circle(screen, self.color, self.pos, self.size)


XMAX = 400
YMAX = 300
size = width, height = XMAX, YMAX
bg_color = pygame.Color(0, 0, 0)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

count = 0
running = True
balls = []
FPS = 100
v = 100  # px / c
d = v // FPS  # FPS * v

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(Ball(event.pos))

    screen.fill(bg_color)
    for ball in balls:
        ball.update(d)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
