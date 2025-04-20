import pygame
from window_values import *
from ingredients import *
from button import *

game_running = True

ingredients_placed = 0
placed_ingredients = []
next_bun_is_top = False
ingredients_current_page = 0

# Initialize Pygame and create a window
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

FONT = pygame.font.Font(None, 36)


def put_ingredients(ingredient: Ingredient) -> None:
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
    global ingredients_current_page
    ingredients_size = (len(INGREDIENTS_LIST)-1) // 6
    ingredients_current_page += (1 if movement == ">" and ingredients_size > ingredients_current_page else -1 if movement == "<" and ingredients_current_page > 0 else 0)
    for index in range(len(INGREDIENTS_LIST)):
        ingredient = INGREDIENTS_LIST[index]
        ingredient.shown =  0 + (ingredients_current_page * 6) <= index < 6 + (ingredients_current_page * 6)


def key_pressed(key) -> None:
    # Majority of the buttons are temporary as they will be replaced with clickable buttons later
    # The keys are mapped to the ingredients for easy access and testing
    global next_bun_is_top, game_running

    match key:
        case pygame.K_ESCAPE:
            game_running = False
        case pygame.K_BACKSPACE:
            print([button.name for button in Button.buttons])
            delete_top_ingredient()


def mouse_pressed(mouse_x: int, mouse_y: int) -> None:
    for button in Button.buttons:
        if button.pressed(mouse_x, mouse_y):
            match button.purpose:
                case Button.PURPOSE_INGREDIENT:
                    print(f"Ingredient {button.name} pressed")
                    put_ingredients(button)
                    break
                case Button.PURPOSE_MOVE_INGREDIENT:
                    print(f"Move ingredient {button.name} pressed")
                    ingredient_navigation(button.name)
                    break
                case Button.PURPOSE_DEFAULT:
                    print(f"Button {button.name} pressed")
                    break


def draw_ingredients_list() -> None:
    for x in range(len(INGREDIENTS_LIST[0 + (ingredients_current_page * 6):6 + (ingredients_current_page * 6)])):
        ingredient = INGREDIENTS_LIST[x + (ingredients_current_page * 6)]

        window.blit(TILE, (ingredient.tile_x, ingredient.tile_y))
        window.blit(ingredient.load_image(), (ingredient.tile_x, ingredient.tile_y + 20))


def draw_placed_ingredients() -> None:
    for index, ingredient in enumerate(placed_ingredients):
        window.blit(ingredient.load_image(), (ingredient.center_x, ingredient.center_y - (GAP * index) + (ingredient.center_y)))


def draw_navigation_arrows() -> None:
    for button in Button.buttons:
        if button.purpose == Button.PURPOSE_MOVE_INGREDIENT and button.shown:
            arrow_text, arrow_rect = button.draw(window, FONT)
            window.blit(arrow_text, arrow_rect)


def draw() -> None:
    # Fill the window with black
    window.fill(BACKGROUND_COLOR)

    # Draw ingredient arrows for navigation
    draw_navigation_arrows()
    
    # Draw the ingredients list
    draw_ingredients_list()

    # Initialize ingredients navigation
    ingredient_navigation("")

    # Draw the placed ingredients
    draw_placed_ingredients()
    
    pygame.display.update()


def main() -> None:
    global game_running
    clock = pygame.time.Clock()

    # Main game loop
    while game_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                key_pressed(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouse_pressed(mouse_x, mouse_y)

        # Draw the window
        draw()

    pygame.quit()
    print("Game closed")

if __name__ == "__main__":
    main()