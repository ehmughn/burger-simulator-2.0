from functionalities.playing import *


def adventure_key_pressed(key) -> None:
    # This function is called when a key is pressed in the adventure game
    playing_key_pressed(key)


def adventure_mouse_pressed(mouse_x: int, mouse_y: int) -> None:
    # This function is called when the mouse is pressed in the adventure game
    playing_mouse_pressed(mouse_x, mouse_y)


def draw_adventure(window) -> None:
    # This function draws the adventure game on the screen
    draw_playing(window)