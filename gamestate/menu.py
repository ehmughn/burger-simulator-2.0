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
        if button.name == "Start":
            Values.current_game_state = Gamestate.ADVENTURE
            Values.browsed_game_state.append(Gamestate.ADVENTURE)
        if button.name == "Recipe Book":
            Values.current_game_state = Gamestate.RECIPE
            Values.browsed_game_state.append(Gamestate.RECIPE)
    print("You pressed the mouse in the menu!")


def draw_game_state_buttons(window, button) -> None:
    color = Color.RED
    font = pygame.font.Font("res/fonts/VAG Rounded Std Bold.otf", 36)
    
    if button.name == "Start":
        color = Color.MAGENTA
        font = pygame.font.Font("res/fonts/VAG Rounded Std Bold.otf", 60)
    elif button.name == "Recipe Book":
        color = Color.CHOCOLATE
        font = pygame.font.Font("res/fonts/VAG Rounded Std Bold.otf", 54)

    arrow_text, arrow_rect = button.draw(window, color=color, font=font, border_radius=20)
    window.blit(arrow_text, arrow_rect)


def draw_buttons(window) -> None:

    allowed_buttons = [Button.PURPOSE_MENU_CHANGE_GAME_STATE]

    for button in Button.buttons:
        if button.purpose not in allowed_buttons:
            continue
        if not button.shown:
            continue
        if button.purpose == Button.PURPOSE_MENU_CHANGE_GAME_STATE:
            draw_game_state_buttons(window, button)


def draw_menu(window) -> None:
    # This function draws the menu on the screen
    window.fill(BACKGROUND_COLOR)

    TITLE_FONT = pygame.font.Font("res/fonts/VAG Rounded Std Bold.otf", 72)
    title = TITLE_FONT.render("Burger Simulator", True, (0,0,0))
    titleRect = title.get_rect()
    titleRect.center = ((WIDTH // 2), 150)
    window.blit(title, titleRect)

    # Draw the buttons on the screen
    draw_buttons(window)

    pygame.display.update()