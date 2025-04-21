from ingredients import *
from button import *
from staticvalues.window_values import *
from staticvalues.colors import Color


ingredients_placed = 0
placed_ingredients = []
next_bun_is_top = False
ingredients_current_page = 0

def put_ingredients(ingredient: Ingredient) -> None:
    # This function is called when an ingredient is placed on the burger
    global ingredients_placed, next_bun_is_top
    ingredients_placed += 1

    if ingredient.name != "Burger Buns":
        placed_ingredients.append(ingredient)
        return
    if next_bun_is_top:
        placed_ingredients.append(burger_buns_top)
    else:
        placed_ingredients.append(burger_buns_bottom)
    next_bun_is_top = not next_bun_is_top


def delete_top_ingredient() -> None:
    # This function is called when the top ingredient is removed from the burger
    if not placed_ingredients:
        return
    
    global ingredients_placed, next_bun_is_top
    removed_ingredient = placed_ingredients.pop()
    if removed_ingredient.name == "Burger Buns Top":
        next_bun_is_top = True
    elif removed_ingredient.name == "Burger Buns Bottom":
        next_bun_is_top = False
    ingredients_placed -= 1


def ingredient_navigation(movement: str) -> None:
    # This function is called when the user navigates through the ingredients list
    global ingredients_current_page
    ingredients_size = (len(INGREDIENTS_LIST)-1) // 6
    if movement == ">":
        if ingredients_current_page < ingredients_size:
            ingredients_current_page += 1
        else:
            ingredients_current_page = 0
    elif movement == "<":
        if ingredients_current_page > 0:
            ingredients_current_page -= 1
        else:
            ingredients_current_page = ingredients_size
    for index in range(len(INGREDIENTS_LIST)):
        ingredient = INGREDIENTS_LIST[index]
        ingredient.shown =  0 + (ingredients_current_page * 6) <= index < 6 + (ingredients_current_page * 6)


def playing_key_pressed(key) -> None:
    # This function is called when the user presses a key on the keyboard
    global next_bun_is_top, game_running

    match key:
        case pygame.K_BACKSPACE:
            delete_top_ingredient()


def playing_mouse_pressed(mouse_x: int, mouse_y: int) -> None:
    # This function is called when the user clicks on the screen
    for button in Button.buttons:
        if not button.pressed(mouse_x, mouse_y):
            continue
        
        match button.purpose:
            case Button.PURPOSE_PLAYING_INGREDIENT:
                put_ingredients(button)
                break
            case Button.PURPOSE_PLAYING_MOVE_INGREDIENT:
                ingredient_navigation(button.name)
                break
            case Button.PURPOSE_DEFAULT:
                break


def draw_ingredients_list(window) -> None:
    # Draw the ingredients list on the screen
    for index in range(len(INGREDIENTS_LIST[0 + (ingredients_current_page * 6):6 + (ingredients_current_page * 6)])):
        ingredient = INGREDIENTS_LIST[index + (ingredients_current_page * 6)]

        window.blit(TILE, (ingredient.tile_x, ingredient.tile_y))
        window.blit(ingredient.load_image(), (ingredient.tile_x, ingredient.tile_y + 15))


def draw_placed_ingredients(window) -> None:
    # Draw the placed ingredients on the screen
    for index, ingredient in enumerate(placed_ingredients):
        window.blit(ingredient.load_image(), (ingredient.center_x, ingredient.center_y - (GAP * index) + (ingredient.center_y)))


def draw_navigation_arrows(window) -> None:
    BIG_FONT = pygame.font.Font("res/fonts/VAG Rounded Std Bold.otf", 72)
    # Draw the navigation arrows on the screen
    for button in Button.buttons:
        if button.purpose == Button.PURPOSE_PLAYING_MOVE_INGREDIENT and button.shown:
            arrow_text, arrow_rect = button.draw(window, color=Color.GREEN, font=BIG_FONT, border_radius=20)
            window.blit(arrow_text, arrow_rect)


def draw_playing(window) -> None:
    # Fill the window with black
    window.fill(BACKGROUND_COLOR)

    # Draw ingredient arrows for navigation
    draw_navigation_arrows(window)
    
    # Draw the ingredients list
    draw_ingredients_list(window)

    # Initialize ingredients navigation
    ingredient_navigation("")

    # Draw the placed ingredients
    draw_placed_ingredients(window)
    
    pygame.display.update()