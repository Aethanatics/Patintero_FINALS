import pygame, os, sys, time
pygame.font.init()

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Patintero!")

MAIN_FONT = pygame.font.SysFont("comicsans", 44)

PURPLE = (125, 77, 176)
BLACK = (0, 0, 0)
BORDER = pygame.Rect(800, 800, 800, 800)

# man i hate math T_T -> left, top, width, and height values
LINE1 = pygame.Rect(WIDTH/2 - 5, 200, 5 , 600) # middle line
LINE2 = pygame.Rect(WIDTH/2 + 300, 200, 5 , 600) # right line
LINE3 = pygame.Rect(WIDTH/2 - 300, 200, 5 , 600) # left line
LINE4 = pygame.Rect(WIDTH/2 - 300, 200, 600 , 5) # horizontal line 1 
LINE5 = pygame.Rect(WIDTH/2 - 300, 400, 600 , 5) # horizontal line 2
LINE6 = pygame.Rect(WIDTH/2 - 300, 600, 600 , 5) # horizontal line 3
LINE7 = pygame.Rect(WIDTH/2 - 300, 800, 605 , 5) # horizontal line 4

FINISHLINE = pygame.Rect(WIDTH/2 - 300, +40, 600 , 70)
OUTSIDEL = pygame.Rect(WIDTH/2 - 400, 200, 100 , 605) # leftside
OUTSIDER = pygame.Rect(WIDTH/2 + 305, 200, 100 , 605) # rightside

FPS = 60
VEL = 5
CHIBI_VELOCITY = 5  # Initial velocity for the chibis

class GameInfo:
    LEVELS = 10

    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        self.level += 1
        self.started = False
        self.level_start_time = time.time()

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS
    
    def start_level(self):
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self):
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)
    
    def get_chibi_velocity(self):
        # Increase chibi velocity for each level
        return CHIBI_VELOCITY + (self.level - 1) * 0.5

def blit_text_center(win, font, text):
    render = font.render(text, 1, (200, 200,200))
    win.blit(render, (win.get_width()/2 - render.get_width()/2, 
                      win.get_height()/2 - render.get_height()/2))


CEMENT = pygame.image.load("assets/cementbg.jpg")

CHIBI_WIDTH, CHIBI_HEIGHT = 120, 120

CHIBI1_IMAGE = pygame.image.load(
    os.path.join('assets', 'sirJLinspired.png'))
CHIBI1 = pygame.transform.scale(
    CHIBI1_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI2_IMAGE = pygame.image.load(
    os.path.join('assets', 'bgyo_akira.png'))
CHIBI2 = pygame.transform.scale(
    CHIBI2_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI3_IMAGE = pygame.image.load(
    os.path.join('assets', 'bgyo_gelo.png'))
CHIBI3 = pygame.transform.scale(
    CHIBI3_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI4_IMAGE = pygame.image.load(
    os.path.join('assets', 'bgyo_jl.png'))
CHIBI4 = pygame.transform.scale(
    CHIBI4_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI5_IMAGE = pygame.image.load(
    os.path.join('assets', 'bgyo_mikki.png'))
CHIBI5 = pygame.transform.scale(
    CHIBI5_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI6_IMAGE = pygame.image.load(
    os.path.join('assets', 'bgyo_nate.png'))
CHIBI6 = pygame.transform.scale(
    CHIBI6_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))



CHIBI1_RECT = CHIBI1.get_rect(topleft=(450, 900))
CHIBI2_RECT = CHIBI2.get_rect(topleft=(150, 900))  
CHIBI3_RECT = CHIBI3.get_rect(topleft=(150, 900))
CHIBI4_RECT = CHIBI4.get_rect(topleft=(150, 900))
CHIBI5_RECT = CHIBI5.get_rect(topleft=(150, 900))
CHIBI6_RECT = CHIBI6.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))


# for chibi1 only
CHIBI1_HITBOX_WIDTH = 6  # Example width
CHIBI1_HITBOX_HEIGHT = 6  # Example height

CHIBI1_HITBOX_RECT = pygame.Rect(
    CHIBI1_RECT.centerx - CHIBI1_HITBOX_WIDTH // 2,
    CHIBI1_RECT.centery - CHIBI1_HITBOX_HEIGHT // 2,
    CHIBI1_HITBOX_WIDTH,
    CHIBI1_HITBOX_HEIGHT
)

def movement_chibi(chibi):
    chibi_rect = chibi["rect"]
    if chibi_rect == CHIBI6_RECT:
        chibi_rect.y += chibi["move_direction"] * CHIBI_VELOCITY
        if chibi_rect.top <= LINE4.top or chibi_rect.bottom >= LINE7.bottom - CHIBI_HEIGHT:
            chibi["move_direction"] *= -1
    else:
        # For other chibis, move horizontally along with CHIBI_VELOCITY
        chibi_rect.x += chibi["move_direction"] * CHIBI_VELOCITY  
    # Change direction if move_counter exceeds 50
        chibi["move_counter"] += 1    
        if chibi["move_counter"] > 115:
            chibi["move_direction"] *= -1
            chibi["move_counter"] = 0

    # Check if chibi is on its respective line and correct its position
    if chibi["rect"] == CHIBI2_RECT:  
        chibi_rect.y = LINE4.top + LINE4.height + 15 - CHIBI_HEIGHT 
    elif chibi["rect"] == CHIBI3_RECT:  
        chibi_rect.y = LINE5.top + LINE5.height + 15 - CHIBI_HEIGHT 
    elif chibi["rect"] == CHIBI4_RECT:  
        chibi_rect.y = LINE6.top + LINE6.height + 15 - CHIBI_HEIGHT
    elif chibi["rect"] == CHIBI5_RECT:  
        chibi_rect.y = LINE7.top + LINE7.height + 15 - CHIBI_HEIGHT
    elif chibi["rect"] == CHIBI6_RECT:  
        chibi_rect.y += chibi["move_direction"] * CHIBI_VELOCITY  # Moving CHIBI6 vertically
        
         # Reverse direction if CHIBI6 reaches the top or bottom of the screen
        if chibi_rect.top <= LINE4.top or chibi_rect.bottom >= LINE7.bottom - CHIBI_HEIGHT:
            chibi["move_direction"] *= -1

def next_level(self, level):
    self.reset()
    self.vel = self.max_vel + (level - 1) * 0.2
    self.current_point = 0

def draw_window(game_info):
    
    pygame.draw.rect(WIN, PURPLE, FINISHLINE)
    pygame.draw.rect(WIN, PURPLE, OUTSIDEL)
    pygame.draw.rect(WIN, PURPLE, OUTSIDER)
    WIN.blit(CEMENT, (0, 0))
    # patintero_stage
    pygame.draw.rect(WIN, BLACK, LINE1)
    pygame.draw.rect(WIN, BLACK, LINE2)
    pygame.draw.rect(WIN, BLACK, LINE3)
    pygame.draw.rect(WIN, BLACK, LINE4)
    pygame.draw.rect(WIN, BLACK, LINE5)
    pygame.draw.rect(WIN, BLACK, LINE6)
    pygame.draw.rect(WIN, BLACK, LINE7)    

    CHIBI_VELOCITY = game_info.get_chibi_velocity()

    level_text = MAIN_FONT.render(f"Level {game_info.level}", 1,(255, 255, 255))
    WIN.blit(level_text, (10, HEIGHT - level_text.get_height() - 950))

    time_text = MAIN_FONT.render(f"Time: {game_info.get_level_time()}s", 1,(255, 255, 255))
    WIN.blit(time_text, (750, HEIGHT - time_text.get_height() - 950))

    #sprites
    WIN.blit(CHIBI1, CHIBI1_RECT)
    WIN.blit(CHIBI2, CHIBI2_RECT)
    WIN.blit(CHIBI3, CHIBI3_RECT)
    WIN.blit(CHIBI4, CHIBI4_RECT)
    WIN.blit(CHIBI5, CHIBI5_RECT)
    WIN.blit(CHIBI6, CHIBI6_RECT)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    chibis = [                                            #width / height or x y
        {"rect": CHIBI2_RECT, "hitbox": CHIBI2_RECT.inflate(-1, -1), "move_direction": 1, "move_counter": 0},
        {"rect": CHIBI3_RECT, "hitbox": CHIBI3_RECT.inflate(-1, -1), "move_direction": 1, "move_counter": 0},
        {"rect": CHIBI4_RECT, "hitbox": CHIBI3_RECT.inflate(-1, -1), "move_direction": 1, "move_counter": 0},
        {"rect": CHIBI5_RECT, "hitbox": CHIBI5_RECT.inflate(-1, -1), "move_direction": 1, "move_counter": 0},
        {"rect": CHIBI6_RECT, "hitbox": CHIBI6_RECT.inflate(-1, -1), "move_direction": 1, "move_counter": 0},
    ]

    game_info = GameInfo()
    run = True
    while run:
        clock.tick(FPS)

        while not game_info.started:
            blit_text_center(
                WIN, MAIN_FONT, f"Press any key to start level {game_info.level}!")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type ==pygame.KEYDOWN:
                    game_info.start_level()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and CHIBI1_RECT.x - VEL + 30 > 0:
            CHIBI1_RECT.x -= VEL
            CHIBI1_HITBOX_RECT.x -= VEL 
        if keys[pygame.K_RIGHT] and CHIBI1_RECT.x + VEL + CHIBI1_RECT.width < BORDER.x + 230  > 0:
            CHIBI1_RECT.x += VEL
            CHIBI1_HITBOX_RECT.x += VEL
        if keys[pygame.K_UP] and CHIBI1_RECT.y - VEL + 20 > 0:
            CHIBI1_RECT.y -= VEL
            CHIBI1_HITBOX_RECT.y -= VEL
        if keys[pygame.K_DOWN] and CHIBI1_RECT.y + VEL + CHIBI1_RECT.height < HEIGHT + 20  > 0:
            CHIBI1_RECT.y += VEL
            CHIBI1_HITBOX_RECT.y += VEL 

        for chibi in chibis:
            if CHIBI1_HITBOX_RECT.colliderect(chibi["rect"]):
                blit_text_center(WIN, MAIN_FONT, "You lost!")
                pygame.display.update()
                print("Game Over")
                pygame.time.wait(3000)
                game_info.reset()
                CHIBI1_RECT.topleft = (450, 900)
                CHIBI1_HITBOX_RECT.topleft = (
                    CHIBI1_RECT.centerx - CHIBI1_HITBOX_WIDTH // 2,
                    CHIBI1_RECT.centery - CHIBI1_HITBOX_HEIGHT // 2
                )

        for outside in [OUTSIDEL, OUTSIDER]:
            if CHIBI1_HITBOX_RECT.colliderect(outside):
                blit_text_center(WIN, MAIN_FONT, "Outside!")
                pygame.display.update()
                print("Outside")
                pygame.time.wait(3000)
                game_info.reset()
                CHIBI1_RECT.topleft = (450, 900)
                CHIBI1_HITBOX_RECT.topleft = (
                    CHIBI1_RECT.centerx - CHIBI1_HITBOX_WIDTH // 2,
                    CHIBI1_RECT.centery - CHIBI1_HITBOX_HEIGHT // 2
                )


            elif CHIBI1_HITBOX_RECT.colliderect(FINISHLINE):
                game_info.next_level()
                blit_text_center(WIN, MAIN_FONT, "You won the game!")
                pygame.display.update()
                print("you win")
                pygame.time.wait(3000)
                game_info.reset()
                CHIBI1_RECT.topleft = (450, 900)
                CHIBI1_HITBOX_RECT.topleft = (
                    CHIBI1_RECT.centerx - CHIBI1_HITBOX_WIDTH // 2,
                    CHIBI1_RECT.centery - CHIBI1_HITBOX_HEIGHT // 2
                )

        for chibi in chibis:
            movement_chibi(chibi)

        draw_window(game_info)

    pygame.quit()

if __name__ == "__main__":
    main()
