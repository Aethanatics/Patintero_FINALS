import pygame
import os

WIDTH, HEIGHT = 700, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Patintero!")

PURPLE = (125, 77, 176)
BLACK = (0, 0, 0)

#man i hate math T_T -> left, top, width, and height values
LINE1 = pygame.Rect(WIDTH/2 - 5, 100, 5 , 600) #middle line
LINE2 = pygame.Rect(WIDTH/2 + 200, 100, 5 , 600) #right line
LINE3 = pygame.Rect(WIDTH/2 - 200, 100, 5 , 600) #left line
LINE4 = pygame.Rect(WIDTH/2 - 200, 100, 400 , 5) #horizontal line 1 
LINE5 = pygame.Rect(WIDTH/2 - 200, 250, 400 , 5) #horizontal line 2
LINE6 = pygame.Rect(WIDTH/2 - 200, 400, 400 , 5) #horizontal line 3
LINE7 = pygame.Rect(WIDTH/2 - 200, 550, 400 , 5) #horizontal line 4
LINE8 = pygame.Rect(WIDTH/2 - 200, 700, 405 , 5) #horizontal line 5


FPS = 60
CHIBI_WIDTH, CHIBI_HEIGHT = 100, 100

CHIBI1_IMAGE = pygame.image.load(
    os.path.join('patintero ASSets', 'Seele_example.png'))
CHIBI1 = pygame.transform.scale(
    CHIBI1_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI2_IMAGE = pygame.image.load(
    os.path.join('patintero ASSets', 'Seele_example1.png'))
CHIBI2 = pygame.transform.scale(
    CHIBI2_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI3_IMAGE = pygame.image.load(
    os.path.join('patintero ASSets', 'Seele_example2.png'))
CHIBI3 = pygame.transform.scale(
    CHIBI3_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI4_IMAGE = pygame.image.load(
    os.path.join('patintero ASSets', 'Seele_example3.png'))
CHIBI4 = pygame.transform.scale(
    CHIBI4_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))

CHIBI1_RECT = CHIBI1.get_rect(topleft=(300, 700))
CHIBI2_RECT = CHIBI2.get_rect(topleft=(150, 620))  
CHIBI3_RECT = CHIBI3.get_rect(topleft=(400, 470))
CHIBI4_RECT = CHIBI3.get_rect(topleft=(300, 320))




def draw_window():
    WIN.fill(PURPLE)
    #patintero_stage
    pygame.draw.rect(WIN, BLACK, LINE1)
    pygame.draw.rect(WIN, BLACK, LINE2)
    pygame.draw.rect(WIN, BLACK, LINE3)
    pygame.draw.rect(WIN, BLACK, LINE4)
    pygame.draw.rect(WIN, BLACK, LINE5)
    pygame.draw.rect(WIN, BLACK, LINE6)
    pygame.draw.rect(WIN, BLACK, LINE7)
    pygame.draw.rect(WIN, BLACK, LINE8)

    WIN.blit(CHIBI1, CHIBI1_RECT)
    WIN.blit(CHIBI2, CHIBI2_RECT)
    WIN.blit(CHIBI3, CHIBI3_RECT)
    WIN.blit(CHIBI4, CHIBI4_RECT)

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

        if keys[pygame.K_a]:
            CHIBI3_RECT.x -= 5
        if keys[pygame.K_d]:
            CHIBI3_RECT.x += 5
        if keys[pygame.K_w]:
            CHIBI3_RECT.y -= 5
        if keys[pygame.K_s]:
            CHIBI3_RECT.y += 5

        if keys[pygame.K_a]:
            CHIBI4_RECT.x -= 5
        if keys[pygame.K_d]:
            CHIBI4_RECT.x += 5
        if keys[pygame.K_w]:
            CHIBI4_RECT.y -= 5
        if keys[pygame.K_s]:
            CHIBI4_RECT.y += 5    

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
