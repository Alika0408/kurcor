import pygame
import os

pygame.init()
WIDTH, HEIGHT = 300, 300
FPS = 60
MOVE_SPEED = 10
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Перемещение персонажа")

hero_image = pygame.image.load(os.path.join('data', 'creature.png'))
hero_rect = hero_image.get_rect(topleft=(0, 0))

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        hero_rect.x -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        hero_rect.x += MOVE_SPEED
    if keys[pygame.K_UP]:
        hero_rect.y -= MOVE_SPEED
    if keys[pygame.K_DOWN]:
        hero_rect.y += MOVE_SPEED

    if hero_rect.x < 0:
        hero_rect.x = 0
    if hero_rect.x > WIDTH - hero_rect.width:
        hero_rect.x = WIDTH - hero_rect.width
    if hero_rect.y < 0:
        hero_rect.y = 0
    if hero_rect.y > HEIGHT - hero_rect.height:
        hero_rect.y = HEIGHT - hero_rect.height

    screen.fill(WHITE)
    screen.blit(hero_image, hero_rect)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
