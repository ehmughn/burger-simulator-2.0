import pygame
from staticvalues.window_values import *
from staticvalues.colors import Color
from staticvalues import gamestate as Gamestate
from button import Button
from globalvalues import *


def menu_key_pressed(key) -> None:
    # This function is called when a key is pressed in the menu
    print("You pressed a key in the menu!")


def menu_mouse_pressed(mouse_x: int, mouse_y: int) -> None:
    # This function is called when the mouse is pressed in the menu
    for button in Button.buttons:
        if not button.pressed(mouse_x, mouse_y):
            continue
        if not button.shown:
            continue
        if button.purpose == Button.PURPOSE_CHANGE_GAME_STATE:
            Values.current_game_state = Gamestate.ADVENTURE
            print(Values.current_game_state)
    print(Values.current_game_state)
    print("You pressed the mouse in the menu!")


def draw_menu(window) -> None:
    # This function draws the menu on the screen
    window.fill((0,0,0))

    BIG_FONT = pygame.font.Font("res/fonts/VAG Rounded Std Bold.otf", 72)

    title = BIG_FONT.render("Play Tic-Tac-Toe", True, (255,255,255))
    titleRect = title.get_rect()
    titleRect.center = ((WIDTH // 2), 150)
    window.blit(title, titleRect)
    
    start_button = Button("Start", (WIDTH//2) - (250//2), 220, 250, 100, Button.PURPOSE_CHANGE_GAME_STATE, shown=True)
    arrow_text, arrow_rect = start_button.draw(window, color=Color.MAGENTA, font=BIG_FONT, border_radius=20)
    window.blit(arrow_text, arrow_rect)

    pygame.display.update()