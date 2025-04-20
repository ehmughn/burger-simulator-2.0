import pygame
from window_values import *
from button import *

GAP = 12


class Ingredient(Button):

    index = 0


    def __init__(self, name: str, image_path: str, uncounted=False, shown=False) -> None:
        self.name = name
        self.image_path = image_path
        self.width = 128
        self.height = 64
        self.center_x = (WIDTH - self.width) // 2
        self.center_y = ((HEIGHT - self.height) // 2) - 128
        self.purpose = Button.PURPOSE_INGREDIENT

        if uncounted:
            return
        
        width_change = (self.index % 6) // 2
        height_change = self.index % 2 == 1

        self.tile_x = 160 + (width_change * (INGREDIENTS_TILE_WIDTH + TILE_WIDTH_GAP)) 
        self.tile_y = HEIGHT - 75 - (INGREDIENTS_TILE_HEIGHT * 2) + (height_change * (INGREDIENTS_TILE_HEIGHT + TILE_HEIGHT_GAP))
        self.tile_width = INGREDIENTS_TILE_WIDTH
        self.tile_height = INGREDIENTS_TILE_HEIGHT

        super().__init__(self.name, self.tile_x + 4, self.tile_y + 30, self.tile_width, self.tile_height + 10, self.purpose)

        Ingredient.index += 1


    def load_image(self):
        image = pygame.image.load("res/ingredients/" + self.image_path + ".png")
        return pygame.transform.scale(image, (self.width, self.height))


# Create instances of Ingredient for each ingredient
bacon = Ingredient("Bacon", "bacon")
burger_buns = Ingredient("Burger Buns", "burger_buns")
burger_buns_bottom = Ingredient("Burger Buns Bottom", "burger_buns_bottom", uncounted=True)
burger_buns_top = Ingredient("Burger Buns Top", "burger_buns_top", uncounted=True)
cheese = Ingredient("Cheese", "cheese")
egg = Ingredient("Egg", "egg")
ketchup = Ingredient("Ketchup", "ketchup")
lettuce = Ingredient("Lettuce", "lettuce")
mango = Ingredient("Mango", "mango")
mayonnaise = Ingredient("Mayonnaise", "mayonnaise")
onion = Ingredient("Onion", "onions")
patty = Ingredient("Patty", "patty")
pickle = Ingredient("Pickle", "pickles")
tomato = Ingredient("Tomato", "tomato")

INGREDIENTS_LIST = [
    bacon,
    burger_buns,
    cheese,
    egg,
    ketchup,
    lettuce,
    mango,
    mayonnaise,
    onion,
    patty,
    pickle,
    tomato
]