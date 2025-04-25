import pygame
from staticvalues.window_values import *
from button import *
from display_adjustments.image import Image

GAP = 12


class Ingredient(Button, Image):

    # Global values about ingredients
    PLACE_LIMIT = 20
    index = 0

    def __init__(self, name: str, image_path: str, uncounted=False, shown=False) -> None:
        
        # Initialize the ingredients attributes
        self.name = name
        self.image_path = image_path
        self.width = 128
        self.height = 64
        self.image = pygame.image.load("res/ingredients/" + self.image_path + ".png")
        self.rect = self.image.get_rect(center=(self.width,self.height))
        self.center_x = (WIDTH - self.width) // 2
        self.center_y = ((HEIGHT - self.height) // 2) - 128
        self.purpose = Button.PURPOSE_PLAYING_INGREDIENT

        # Filters out which ingredients is actually displayed in the selectable ingredients
        if uncounted:
            return
        
        # Width and height measurements in the selectable ingredients
        width_change = (self.index % 6) // 2
        height_change = self.index % 2 == 1

        self.tile_x = 190 + (width_change * (INGREDIENTS_TILE_WIDTH + TILE_WIDTH_GAP)) 
        self.tile_y = HEIGHT - 75 - (INGREDIENTS_TILE_HEIGHT * 2) + (height_change * (INGREDIENTS_TILE_HEIGHT + TILE_HEIGHT_GAP))
        self.tile_width = INGREDIENTS_TILE_WIDTH
        self.tile_height = INGREDIENTS_TILE_HEIGHT

        # calls the parent button class to make the ingredient a button
        # super().__init__(self.name, self.tile_x + 4, self.tile_y + 15, self.tile_width, self.tile_height + 10, self.purpose)

        self.name = name
        self.x = self.tile_x + 4
        self.y = self.tile_y + 15
        self.height = self.height + 10
        self.shown = False
        Button.buttons.append(self)

        Ingredient.index += 1


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
mustard = Ingredient("Mustard", "mustard")
mayonnaise = Ingredient("Mayonnaise", "mayonnaise")
onion = Ingredient("Onion", "onions")
patty = Ingredient("Patty", "patty")
pickle = Ingredient("Pickle", "pickles")
tomato = Ingredient("Tomato", "tomato")

# List out the whole list of ingredients
INGREDIENTS_LIST = [
    bacon,
    burger_buns,
    cheese,
    egg,
    ketchup,
    lettuce,
    mango,
    mustard,
    mayonnaise,
    onion,
    patty,
    pickle,
    tomato
]

# This list shows what the user is currently owned
owned_ingredients: list[Ingredient] = []

# Temporarily sets the owned ingredients to INGREDIENTS_LIST (whole list of ingredients)
# for debugging purposes
owned_ingredients = INGREDIENTS_LIST