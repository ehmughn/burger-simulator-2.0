import pygame
import window_values
import ingredients

ingredients_placed = 0
placed_ingredients = []
next_bun_is_top = False

# Initialize Pygame and create a window
pygame.init()
window = pygame.display.set_mode((window_values.WIDTH, window_values.HEIGHT))
pygame.display.set_caption(window_values.TITLE)

def put_ingredients(ingredient: ingredients.Ingredient) -> None:
    global ingredients_placed
    placed_ingredients.append(ingredient)
    window.blit(ingredient.load_image(), (ingredient.center_x, ingredient.center_y - (25 * ingredients_placed) + (ingredient.center_y // 2)))
    ingredients_placed += 1

def delete_top_ingredient() -> None:
    global ingredients_placed, next_bun_is_top
    if placed_ingredients:
        removed_ingredient = placed_ingredients.pop()
        if removed_ingredient.name == "Burger Buns Top":
            next_bun_is_top = True
        elif removed_ingredient.name == "Burger Buns Bottom":
            next_bun_is_top = False
        ingredients_placed -= 1
        redraw_ingredients()

def redraw_ingredients() -> None:
    window.fill((0, 0, 0))
    for index, ingredient in enumerate(placed_ingredients):
        window.blit(ingredient.load_image(), (ingredient.center_x, ingredient.center_y - (25 * index) + (ingredient.center_y // 2)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_q:
                if next_bun_is_top:
                    put_ingredients(ingredients.burger_buns_top)
                else:
                    put_ingredients(ingredients.burger_buns_bottom)
                next_bun_is_top = not next_bun_is_top
            elif event.key == pygame.K_w:
                put_ingredients(ingredients.bacon)
            elif event.key == pygame.K_e:
                put_ingredients(ingredients.cheese)
            elif event.key == pygame.K_r:
                put_ingredients(ingredients.egg)
            elif event.key == pygame.K_t:
                put_ingredients(ingredients.ketchup)
            elif event.key == pygame.K_y:
                put_ingredients(ingredients.lettuce)
            elif event.key == pygame.K_u:
                put_ingredients(ingredients.mango)
            elif event.key == pygame.K_i:
                put_ingredients(ingredients.mayonnaise)
            elif event.key == pygame.K_o:
                put_ingredients(ingredients.onion)
            elif event.key == pygame.K_a:
                put_ingredients(ingredients.patty)
            elif event.key == pygame.K_s:
                put_ingredients(ingredients.pickle)
            elif event.key == pygame.K_d:
                put_ingredients(ingredients.tomato)
            elif event.key == pygame.K_BACKSPACE:
                delete_top_ingredient()
    
    pygame.display.update()
pygame.quit()
print("Game closed")