import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("курсор")

cursor_image = pygame.image.load("data/arrow.png").convert_alpha()

pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    if pygame.mouse.get_focused():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(cursor_image, (mouse_x - cursor_image.get_width() // 2, mouse_y - cursor_image.get_height() // 2))
    pygame.display.flip()
