import pygame, sys, os, sqlite3, maincode
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("BGYO!")

BG = pygame.image.load("assets/BGYO.png")

pygame.mixer.music.load("assets/BG_music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    pygame.display.set_caption("Patintero")
    maincode.main()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")

        conn = sqlite3.connect('scores.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)''')
        c.execute("SELECT * FROM scores")
        scores_data = c.fetchall()
        conn.close()

        num_scores = len(scores_data)

        for i in range(num_scores):
            name = scores_data[i][0]
            score = scores_data[i][1]

            score_text = get_font(25).render(f"Name: {name.ljust(10)} Score: {str(score).rjust(1)}", True, "Black")
            score_rect = score_text.get_rect(center=(400, 200 + 50 * i))
            SCREEN.blit(score_text, score_rect)

            delete_button = Button(image=None, pos=(900, 200 + 50 * i),
                                   text_input="DELETE", font=get_font(10), base_color="Red", hovering_color="DarkRed")
            delete_button.changeColor(OPTIONS_MOUSE_POS)
            delete_button.update(SCREEN)

            if delete_button.rect.collidepoint(OPTIONS_MOUSE_POS):
                if pygame.mouse.get_pressed()[0]:
                    confirm_message = get_font(20).render("Are you sure you want to delete this? Y/N", True, "Black")
                    confirm_rect = confirm_message.get_rect(center=(500, 250 + 50 * i))
                    SCREEN.blit(confirm_message, confirm_rect)
                    pygame.display.update()

                    waiting_for_confirmation = True
                    while waiting_for_confirmation:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    conn = sqlite3.connect('scores.db')
                                    c = conn.cursor()
                                    c.execute("DELETE FROM scores WHERE name = ? AND score = ?", (name, score))
                                    conn.commit()
                                    conn.close()
                                    waiting_for_confirmation = False
                                elif event.key == pygame.K_n:
                                    waiting_for_confirmation = False

        OPTIONS_BACK = Button(image=None, pos=(500, 860), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("BGYO!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(500, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(500, 400), 
                            text_input="SCORES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(500, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return_to_menu = maincode.main()
                    if not return_to_menu:
                        pygame.quit()
                        sys.exit()
                    pygame.display.update()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

''' 
NOTES: owo)b

Line 1-15: Literal
Line 18: to start the maincode
Line 36-47: Para ma display yung scores and uh delete buttons
Line 50-71: confirmation message 
Line 89: Main menu na ginawang def(function) 
Line 129: Calls the main menu to run
'''