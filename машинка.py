import pygame
import os

pygame.init()

WIDTH, HEIGHT = 600, 95
FPS = 60
SPEED = 5
WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('data', 'car2.png'))
        self.image = pygame.transform.scale(self.image, (50, 30))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.direction = 1

    def update(self):
        self.rect.x += self.direction * SPEED
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.direction *= -1
            self.image = pygame.transform.flip(self.image, True, False)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Перемещение машинки")

all_sprites = pygame.sprite.Group()
car = Car()
all_sprites.add(car)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
