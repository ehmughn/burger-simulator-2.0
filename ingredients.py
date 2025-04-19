import pygame
import window_values

class Ingredient:
    def __init__(self, name: str, image_path: str):
        self.name = name
        self.image_path = image_path
        self.width = 128
        self.height = 64
        self.center_x = (window_values.WIDTH - self.width) // 2
        self.center_y = (window_values.HEIGHT - self.height) // 2

    def load_image(self):
        image = pygame.image.load("res/ingredients/" + self.image_path + ".png")
        return pygame.transform.scale(image, (self.width, self.height))

# Create instances of Ingredient for each ingredient
bacon = Ingredient("Bacon", "bacon")
burger_buns_bottom = Ingredient("Burger Buns Bottom", "burger_buns_bottom")
burger_buns_top = Ingredient("Burger Buns Top", "burger_buns_top")
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