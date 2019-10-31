from src.interactables.Interactable import Interactable
from src.Game import GameState
class Window(Interactable):
    def __init__(self):
        Interactable.__init__(self, "window", "You open the window to freedom. Very well done! You win!")
    
    def trigger(self, game):
        super().trigger(game)
        game.game_state = GameState.MENU