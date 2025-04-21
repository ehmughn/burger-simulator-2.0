import pygame
from ingredients import *
from button import *
from staticvalues.window_values import *
from globalvalues import *

from staticvalues import gamestate as Gamestate
from gamestate.menu import draw_menu, menu_key_pressed, menu_mouse_pressed
from gamestate.adventure import draw_adventure, adventure_key_pressed, adventure_mouse_pressed
from gamestate.recipe import draw_recipe, recipe_key_pressed, recipe_mouse_pressed

# Initialize Pygame and create a window
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

FONT = pygame.font.Font("res/fonts/VAG Rounded Std Bold.otf", 36)
BIG_FONT = pygame.font.Font("res/fonts/VAG Rounded Std Bold.otf", 72)


def map_mouse_press(mouse_x, mouse_y) -> None:
    # This function is called when the mouse is pressed globally
    # It maps the mouse press to the current game state
    # and calls the appropriate function
    match Values.current_game_state:
        case Gamestate.MENU:
            menu_mouse_pressed(mouse_x, mouse_y)
        case Gamestate.ADVENTURE:
            adventure_mouse_pressed(mouse_x, mouse_y)
        case Gamestate.RECIPE:
            recipe_mouse_pressed(mouse_x, mouse_y)



def map_key_press(key) -> None:
    # This function is called when a key is pressed globally
    # It maps the key press to the current game state
    # and calls the appropriate function
    # It also handles the ESC key to exit the game and debugging features
    
    if key == pygame.K_ESCAPE:
        Values.game_running = False
        return
    elif key == pygame.K_1:
        Values.current_game_state = Gamestate.MENU
        return
    elif key == pygame.K_2:
        Values.current_game_state = Gamestate.ADVENTURE
        return
    elif key == pygame.K_3:
        Values.current_game_state = Gamestate.RECIPE
        return
    elif key == pygame.K_d:
        print("Debugging key pressed")
        print(f"Current game state: {Values.current_game_state}")
        return
    match Values.current_game_state:
        case Gamestate.MENU:
            menu_key_pressed(key)
        case Gamestate.ADVENTURE:
            adventure_key_pressed(key)
        case Gamestate.RECIPE:
            recipe_key_pressed(key)


def main() -> None:
    # Initialize the game state and ingredients
    clock = pygame.time.Clock()

    # Main game loop
    while Values.game_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Values.game_running = False
            elif event.type == pygame.KEYDOWN:
                map_key_press(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                map_mouse_press(mouse_x, mouse_y)

        # Draw the window
        match Values.current_game_state:
            case Gamestate.MENU:
                draw_menu(window)
            case Gamestate.ADVENTURE:
                draw_adventure(window)
            case Gamestate.RECIPE:
                draw_recipe(window)

    pygame.quit()
    print("Game closed")

if __name__ == "__main__":
    main()