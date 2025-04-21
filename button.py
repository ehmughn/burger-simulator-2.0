import pygame
from staticvalues.window_values import *
from staticvalues.colors import Color

class Button:

    PURPOSE_DEFAULT = 0
    PURPOSE_PLAYING_INGREDIENT = 1
    PURPOSE_PLAYING_MOVE_INGREDIENT = 2
    PURPOSE_MENU_CHANGE_GAME_STATE = 3
    PURPOSE_RECIPE_MOVE_RECIPE = 4

    buttons = []

    def __init__(self, name, x, y, width, height, purpose=PURPOSE_DEFAULT, shown=False):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.purpose = purpose
        self.shown = shown
        Button.buttons.append(self)


    def __str__(self) -> str:
        return f"Button(name={self.name})"
    

    def draw(self, window, font, color=Color.RED, border_radius=0):
        if self.shown:
            arrow_text = font.render(self.name, True, (255, 255, 255))
            arrow_button = pygame.Rect(self.x, self.y, self.width, self.height)
            arrow_rect = arrow_text.get_rect()
            arrow_rect.center = arrow_button.center
            pygame.draw.rect(window, color, arrow_button, border_radius=border_radius)
            return arrow_text, arrow_rect


    def pressed(self, mouse_x, mouse_y):
        return self.shown and (self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height)
    
    
    def __repr__(self) -> str:
        return f"{self.name}: {self.purpose}"



Button("<", 70, 470, 100, 100, Button.PURPOSE_PLAYING_MOVE_INGREDIENT, shown=True)
Button(">", WIDTH - 170, 470, 100, 100, Button.PURPOSE_PLAYING_MOVE_INGREDIENT, shown=True)
    
start_button = Button("Start", (WIDTH//2) - (200//2), 220, 200, 80, Button.PURPOSE_MENU_CHANGE_GAME_STATE, shown=True)
recipe_button = Button("Recipe Book", (WIDTH//2) - (300//2), 320, 300, 80, Button.PURPOSE_MENU_CHANGE_GAME_STATE, shown=True)

Button("<", 70, 470, 100, 100, Button.PURPOSE_RECIPE_MOVE_RECIPE, shown=True)
Button(">", WIDTH - 170, 470, 100, 100, Button.PURPOSE_RECIPE_MOVE_RECIPE, shown=True)