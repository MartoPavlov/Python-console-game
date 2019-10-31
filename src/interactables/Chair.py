from src.interactables.Interactable import Interactable
class Chair(Interactable):
    def __init__(self):
        Interactable.__init__(self, "chair", "Sitting down. You feel rested.")

    def trigger(self, game):
        super().trigger(game)
