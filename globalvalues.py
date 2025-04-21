from staticvalues import gamestate as Gamestate

class Values:
    # This class holds the global values for the game
    current_game_state = Gamestate.MENU
    browsed_game_state = [Gamestate.MENU]

    game_running = True