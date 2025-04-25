import pygame
from staticvalues.window_values import *
from staticvalues.colors import Color
from staticvalues import gamestate as Gamestate
from button import Button
from globalvalues import *

from staticvalues.burger_recipes import owned_recipes
from ingredients import GAP

current_page = 0

def recipe_navigation(movement: str) -> None:
    # This function is called when the user navigates through the recipe book
    global current_page
    book_size = (len(owned_recipes)-1) // 2
    if movement == ">":
        if current_page < book_size:
            current_page += 1
        else:
            current_page = 0
    elif movement == "<":
        if current_page > 0:
            current_page -= 1
        else:
            current_page = book_size

def draw_navigation_arrows(window) -> None:
    BIG_FONT = pygame.font.Font("res/fonts/VAG Rounded Std Bold.otf", 72)
    # Draw the navigation arrows on the screen
    for button in Button.buttons:
        if button.purpose == Button.PURPOSE_RECIPE_MOVE_RECIPE and button.shown:
            arrow_text, arrow_rect = button.draw(window, color=Color.GREEN, font=BIG_FONT, border_radius=20)
            window.blit(arrow_text, arrow_rect)


def draw_page_label(window) -> None:
    # This function draws the current page of the recipe book
    PAGE_FONT = pygame.font.Font("res/fonts/VAG Rounded Std Bold.otf", 72)
    label = PAGE_FONT.render(f"{current_page + 1}/3", True, (255,255,255))
    labelRect = label.get_rect()
    labelRect.center = (WIDTH // 2, 520)
    window.blit(label, labelRect)


def draw_burger(window, burger, is_left) -> None:
    # This function draws the burger recipe in the recipe book
    gap = 0
    left_or_right = 0 if is_left else 1
    for index, ingredient in enumerate(burger):
        window.blit(ingredient.transform_image(128,64), (140 + (400 * left_or_right), ingredient.center_y - (GAP * index) + (ingredient.center_y)))


def draw_burgers(window) -> None:
    # This function sets up what burger recipe to draw
    
    for index in range(len(owned_recipes[0 + (current_page * 2):2 + (current_page * 2)])):

        # Draw the burger recipe
        draw_burger(window, owned_recipes[index + (current_page * 2)][1], index % 2 == 0)

        # Put label to the recipe
        RECIPE_FONT = pygame.font.Font("res/fonts/VAG Rounded Std Bold.otf", 36)
        label = RECIPE_FONT.render(owned_recipes[index + (current_page * 2)][0], True, (255,255,255))
        labelRect = label.get_rect()
        labelRect.center = ((WIDTH // 2) + ((WIDTH // 4) * (-1 if index % 2 == 0 else 1)), 400)
        window.blit(label, labelRect)


def recipe_key_pressed(key) -> None:
    # This function is called when a key is pressed in the recipe book
    print("You pressed a key in the recipe book!")


def recipe_mouse_pressed(mouse_x: int, mouse_y: int) -> None:
    # This function is called when mouse is pressed in the recipe book
    for button in Button.buttons:
        if not button.pressed(mouse_x, mouse_y):
            continue
        
        match button.purpose:
            case Button.PURPOSE_PLAYING_MOVE_INGREDIENT:
                recipe_navigation(button.name)
                break
            case Button.PURPOSE_DEFAULT:
                break


def draw_recipe(window) -> None:
    # This function draws the recipe book on the screen
    window.fill((0,0,0))

    # Draw ingredient arrows for navigation
    draw_navigation_arrows(window)

    # Draw page label
    draw_page_label(window)

    # This function draws the burgers
    draw_burgers(window)
    
    pygame.display.update()