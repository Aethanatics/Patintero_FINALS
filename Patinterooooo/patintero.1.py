import pygame
import os

WIDTH, HEIGHT = 700, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Patintero!")

PURPLE = (125, 77, 176)
BLACK = (0, 0, 0)

FPS = 60
CHIBI_WIDTH, CHIBI_HEIGHT = 200, 200

CHIBI1_IMAGE = pygame.image.load(
    os.path.join('patintero ASSets', 'Seele_example.png'))
CHIBI1 = pygame.transform.scale(
    CHIBI1_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI2_IMAGE = pygame.image.load(
    os.path.join('patintero ASSets', 'Raiden_example.png'))
CHIBI2 = pygame.transform.scale(
    CHIBI2_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))

CHIBI1_RECT = CHIBI1.get_rect(topleft=(300, 100))
CHIBI2_RECT = CHIBI2.get_rect(topleft=(100, 100))

def draw_window():
    WIN.fill(PURPLE)
    WIN.blit(CHIBI1, CHIBI1_RECT)
    WIN.blit(CHIBI2, CHIBI2_RECT)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            CHIBI1_RECT.x -= 5
        if keys[pygame.K_RIGHT]:
            CHIBI1_RECT.x += 5
        if keys[pygame.K_UP]:
            CHIBI1_RECT.y -= 5
        if keys[pygame.K_DOWN]:
            CHIBI1_RECT.y += 5

        if keys[pygame.K_a]:
            CHIBI2_RECT.x -= 5
        if keys[pygame.K_d]:
            CHIBI2_RECT.x += 5
        if keys[pygame.K_w]:
            CHIBI2_RECT.y -= 5
        if keys[pygame.K_s]:
            CHIBI2_RECT.y += 5

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
