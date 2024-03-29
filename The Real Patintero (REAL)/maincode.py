import pygame, os, sys, time, sqlite3

pygame.font.init()

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Patintero!")

MAIN_FONT = pygame.font.SysFont("comicsans", 44)

PURPLE = (125, 77, 176)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(800, 800, 800, 800)
LINE1 = pygame.Rect(WIDTH/2 - 5, 200, 5 , 600)
LINE2 = pygame.Rect(WIDTH/2 + 300, 200, 5 , 600)
LINE3 = pygame.Rect(WIDTH/2 - 300, 200, 5 , 600)
LINE4 = pygame.Rect(WIDTH/2 - 300, 200, 600 , 5)
LINE5 = pygame.Rect(WIDTH/2 - 300, 400, 600 , 5)
LINE6 = pygame.Rect(WIDTH/2 - 300, 600, 600 , 5)
LINE7 = pygame.Rect(WIDTH/2 - 300, 800, 605 , 5)
FINISHLINE = pygame.Rect(WIDTH/2 - 300, +40, 600 , 70)
OUTSIDEL = pygame.Rect(WIDTH/2 - 400, 200, 100 , 605)
OUTSIDER = pygame.Rect(WIDTH/2 + 305, 200, 100 , 605)

FPS = 60
VEL = 5
CHIBI_VELOCITY = 5 

class GameInfo:
    LEVELS = 100

    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0
        self.score = 0

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
        
    def score_add(self):
        self.score += 1
    
    def score_reset(self):
        self.score = 0
    
    def save_score(self, player_name):
        conn = sqlite3.connect('scores.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)''')
        score = self.score
        c.execute("INSERT INTO scores VALUES (?, ?)", (player_name, score))
        conn.commit()
        conn.close()
    
    def view_scores(self):
        conn = sqlite3.connect('scores.db')
        c = conn.cursor()
        c.execute("SELECT * FROM scores")
        data = c.fetchall()
        print("Scores:")
        for row in data:
            print(f"Name: {row[0]}, Score: {row[1]}")
        conn.close()

    def delete_score(self):
        conn = sqlite3.connect('scores.db')
        c = conn.cursor()
        c.execute("DELETE FROM scores WHERE ROWID = (SELECT min(ROWID) FROM scores)")
        conn.commit()
        conn.close()

def blit_text_center(win, font, text):
    render = font.render(text, 1, (200, 200,200))
    win.blit(render, (win.get_width()/2 - render.get_width()/2, 
                      win.get_height()/2 - render.get_height()/2))

def text_input_box(win, font, text, text_input):
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width()/2 - render.get_width()/2, 
                      win.get_height()/2 - render.get_height()/2 - 50))
    pygame.draw.rect(win, (255, 255, 255), (win.get_width()/2 - 150, 
                                             win.get_height()/2 + 20, 300, 50), 2)
    text_surf = font.render(text_input, 1, (255, 255, 255))
    win.blit(text_surf, (win.get_width()/2 - text_surf.get_width()/2, 
                         win.get_height()/2 + 10))

def input_name():
    run = True
    name = ""
    while run:
        WIN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 10:  # Limit input to 10 characters
                    name += event.unicode
        text_input_box(WIN, MAIN_FONT, "Enter Your Name:", name)
        pygame.display.update()
    return name

CEMENT = pygame.image.load("assets/cementbg.jpg")

CHIBI_WIDTH, CHIBI_HEIGHT = 120, 120

CHIBI1_IMAGE = pygame.image.load(os.path.join('assets', 'sirJLinspired.png'))
CHIBI1 = pygame.transform.scale(CHIBI1_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI2_IMAGE = pygame.image.load(os.path.join('assets', 'bgyo_akira.png'))
CHIBI2 = pygame.transform.scale(CHIBI2_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI3_IMAGE = pygame.image.load(os.path.join('assets', 'bgyo_gelo.png'))
CHIBI3 = pygame.transform.scale(CHIBI3_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI4_IMAGE = pygame.image.load(os.path.join('assets', 'bgyo_jl.png'))
CHIBI4 = pygame.transform.scale(CHIBI4_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI5_IMAGE = pygame.image.load(os.path.join('assets', 'bgyo_mikki.png'))
CHIBI5 = pygame.transform.scale(CHIBI5_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))
CHIBI6_IMAGE = pygame.image.load(os.path.join('assets', 'bgyo_nate.png'))
CHIBI6 = pygame.transform.scale(CHIBI6_IMAGE, (CHIBI_WIDTH, CHIBI_HEIGHT))

CHIBI1_RECT = CHIBI1.get_rect(topleft=(440, 900))
CHIBI2_RECT = CHIBI2.get_rect(topleft=(150, 900))  
CHIBI3_RECT = CHIBI3.get_rect(topleft=(150, 900))
CHIBI4_RECT = CHIBI4.get_rect(topleft=(150, 900))
CHIBI5_RECT = CHIBI5.get_rect(topleft=(150, 900))
CHIBI6_RECT = CHIBI6.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))

CHIBI1_HITBOX_WIDTH = 6
CHIBI1_HITBOX_HEIGHT = 6
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
        chibi_rect.x += chibi["move_direction"] * CHIBI_VELOCITY
        chibi["move_counter"] += 1    
        if chibi["move_counter"] > 115:
            chibi["move_direction"] *= -1
            chibi["move_counter"] = 0

    if chibi["rect"] == CHIBI2_RECT:  
        chibi_rect.y = LINE4.top + LINE4.height + 15 - CHIBI_HEIGHT 
    elif chibi["rect"] == CHIBI3_RECT:  
        chibi_rect.y = LINE5.top + LINE5.height + 15 - CHIBI_HEIGHT 
    elif chibi["rect"] == CHIBI4_RECT:  
        chibi_rect.y = LINE6.top + LINE6.height + 15 - CHIBI_HEIGHT
    elif chibi["rect"] == CHIBI5_RECT:  
        chibi_rect.y = LINE7.top + LINE7.height + 15 - CHIBI_HEIGHT
    elif chibi["rect"] == CHIBI6_RECT:  
        chibi_rect.y += chibi["move_direction"] * CHIBI_VELOCITY  
        if chibi_rect.top <= LINE4.top or chibi_rect.bottom >= LINE7.bottom - CHIBI_HEIGHT:
            chibi["move_direction"] *= -1

chibis = [
    {"rect": CHIBI2_RECT, "hitbox": CHIBI2_RECT.inflate(-1, -1), "move_direction": 1, "move_counter": 0},
    {"rect": CHIBI3_RECT, "hitbox": CHIBI3_RECT.inflate(-1, -1), "move_direction": 1, "move_counter": 0},
    {"rect": CHIBI4_RECT, "hitbox": CHIBI3_RECT.inflate(-1, -1), "move_direction": 1, "move_counter": 0},
    {"rect": CHIBI5_RECT, "hitbox": CHIBI5_RECT.inflate(-1, -1), "move_direction": 1, "move_counter": 0},
    {"rect": CHIBI6_RECT, "hitbox": CHIBI6_RECT.inflate(-1, -1), "move_direction": 1, "move_counter": 0},
]

def reset_chibi_positions():
    CHIBI2_RECT.topleft = (150, 900)
    CHIBI3_RECT.topleft = (150, 900)
    CHIBI4_RECT.topleft = (150, 900)
    CHIBI5_RECT.topleft = (150, 900)
    for chibi in chibis:
        if chibi["rect"] != CHIBI6_RECT:
            chibi["move_direction"] = 1
            chibi["move_counter"] = 0

def draw_window(game_info, player_name):
    pygame.draw.rect(WIN, PURPLE, FINISHLINE)
    pygame.draw.rect(WIN, PURPLE, OUTSIDEL)
    pygame.draw.rect(WIN, PURPLE, OUTSIDER)
    WIN.blit(CEMENT, (0, 0)) #para maconceal yung hitbox owo)b
    pygame.draw.rect(WIN, BLACK, LINE1)
    pygame.draw.rect(WIN, BLACK, LINE2)
    pygame.draw.rect(WIN, BLACK, LINE3)
    pygame.draw.rect(WIN, BLACK, LINE4)
    pygame.draw.rect(WIN, BLACK, LINE5)
    pygame.draw.rect(WIN, BLACK, LINE6)
    pygame.draw.rect(WIN, BLACK, LINE7)    
    level_text = MAIN_FONT.render(f"Level {game_info.level}", 1,(255, 255, 255))
    WIN.blit(level_text, (10, HEIGHT - level_text.get_height() - 950))
    time_text = MAIN_FONT.render(f"Time: {game_info.get_level_time()}s", 1,(255, 255, 255))
    WIN.blit(time_text, (750, HEIGHT - time_text.get_height() - 950))
    WIN.blit(CHIBI1, CHIBI1_RECT)
    WIN.blit(CHIBI2, CHIBI2_RECT)
    WIN.blit(CHIBI3, CHIBI3_RECT)
    WIN.blit(CHIBI4, CHIBI4_RECT)
    WIN.blit(CHIBI5, CHIBI5_RECT)
    WIN.blit(CHIBI6, CHIBI6_RECT)
    pygame.display.update()

def main_menu():
    import mainmenu
    mainmenu.main_menu()

def main():
    clock = pygame.time.Clock()
    game_info = GameInfo()
    run = True
    while run:
        clock.tick(FPS)
        while not game_info.started:
            WIN.fill("black")
            blit_text_center(
                WIN, MAIN_FONT, f"Press any key to start level {game_info.level}!")
            reset_chibi_positions()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    game_info.start_level()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                WIN.fill(BLACK)
                blit_text_center(WIN, MAIN_FONT, "Return to main menu? Y/N")
                pygame.display.update()
                choice_made = False
                while not choice_made:
                    for inner_event in pygame.event.get():
                        if inner_event.type == pygame.KEYDOWN:
                            if inner_event.key == pygame.K_y:
                                main_menu()
                                choice_made = True
                            elif inner_event.key == pygame.K_n:
                                choice_made = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and CHIBI1_RECT.x - VEL + 30 > 0:
            CHIBI1_RECT.x -= VEL
            CHIBI1_HITBOX_RECT.x -= VEL 
        if keys[pygame.K_d] and CHIBI1_RECT.x + VEL + CHIBI1_RECT.width < BORDER.x + 230  > 0:
            CHIBI1_RECT.x += VEL
            CHIBI1_HITBOX_RECT.x += VEL
        if keys[pygame.K_w] and CHIBI1_RECT.y - VEL + 20 > 0:
            CHIBI1_RECT.y -= VEL
            CHIBI1_HITBOX_RECT.y -= VEL
        if keys[pygame.K_s] and CHIBI1_RECT.y + VEL + CHIBI1_RECT.height < HEIGHT + 20  > 0:
            CHIBI1_RECT.y += VEL
            CHIBI1_HITBOX_RECT.y += VEL
        if keys[pygame.K_ESCAPE]:
            run = False
            main_menu()
        if keys[pygame.K_l]:
            game_info.view_scores()
        for chibi in chibis:
            if CHIBI1_HITBOX_RECT.colliderect(chibi["rect"]):
                WIN.fill("black")
                blit_text_center(WIN, MAIN_FONT, "You've been tagged!")
                pygame.display.update()
                pygame.time.wait(2000)
                player_name = input_name()
                game_info.save_score(player_name)
                game_info.score_reset()
                reset_chibi_positions()
                print("Game Over")
                pygame.time.wait(2000)
                game_info.reset()
                CHIBI1_RECT.topleft = (440, 900)
                CHIBI1_HITBOX_RECT.topleft = (
                    CHIBI1_RECT.centerx - CHIBI1_HITBOX_WIDTH // 2,
                    CHIBI1_RECT.centery - CHIBI1_HITBOX_HEIGHT // 2
                )
        for outside in [OUTSIDEL, OUTSIDER]:
            if CHIBI1_HITBOX_RECT.colliderect(outside):
                WIN.fill("black")
                blit_text_center(WIN, MAIN_FONT, "Outside!")
                pygame.display.update()
                pygame.time.wait(2000)
                player_name = input_name()
                game_info.save_score(player_name)
                game_info.score_reset()
                print("Outside")
                game_info.reset()
                reset_chibi_positions()
                CHIBI1_RECT.topleft = (440, 900)
                CHIBI1_HITBOX_RECT.topleft = (
                    CHIBI1_RECT.centerx - CHIBI1_HITBOX_WIDTH // 2,
                    CHIBI1_RECT.centery - CHIBI1_HITBOX_HEIGHT // 2
                )
            elif CHIBI1_HITBOX_RECT.colliderect(FINISHLINE):
                WIN.fill("black")
                game_info.score_add()
                blit_text_center(WIN, MAIN_FONT, f"You beat Level {game_info.level}! Score: {game_info.score}")
                pygame.display.update()
                print("you win")
                pygame.time.wait(3000)
                game_info.next_level()
                reset_chibi_positions()
                CHIBI1_RECT.topleft = (440, 900)
                CHIBI1_HITBOX_RECT.topleft = (
                    CHIBI1_RECT.centerx - CHIBI1_HITBOX_WIDTH // 2,
                    CHIBI1_RECT.centery - CHIBI1_HITBOX_HEIGHT // 2
                )
        for chibi in chibis:
            movement_chibi(chibi)
        draw_window(game_info, "")
    pygame.quit()

if __name__ == "__main__":
    main()

'''
NOTES: owo)b

Line 5-7: yung window and yung caption
Line 14-24: ownmade patintero lines and boundaries na rin
Line 30-91: Class para ma store yung game information & funcitonality na ri
Line 93-106: display text in center, also displays text box
Line 108-126: player name input
Line 128-159: Load the imgaes of BG and chibis(sprites) and also the position of it
Line 161-203: movement functions for the chibis 
Line 205-227: To draw the OWNMADE patintero lines & text
Line 268-280: WASD movement 
Line 286-333: the initialization of hitbox on what happens if its reaches/collides the hitbox...
'''