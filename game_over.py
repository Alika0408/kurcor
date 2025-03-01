import pygame
import os

pygame.init()

WIDTH, HEIGHT = 600, 300
FPS = 60
SPEED = 200
BLUE = (0, 0, 255)

image = pygame.image.load(os.path.join('data', 'gamee.png'))
image_rect = image.get_rect(topleft=(-image.get_width(), HEIGHT // 2 - image.get_height() // 2))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME OVER")

running = True
clock = pygame.time.Clock()
moving = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if moving:
        image_rect.x += SPEED / FPS
        if image_rect.right >= WIDTH:
            moving = False
    screen.fill(BLUE)
    screen.blit(image, image_rect)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
