from src.interactables.Interactable import Interactable

class Door(Interactable):
    def __init__(self):
        Interactable.__init__(self, "door", "Normal wooden door. You open it.")
    
    def trigger(self, game):
        super().trigger(game)
        game.player.currRoom+=1