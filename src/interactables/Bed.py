from src.interactables.Interactable import Interactable
class Bed(Interactable):
    def __init__(self):
        Interactable.__init__(self, "bed", "You lay down on the bed...It's comfy!")

    def trigger(self, game):
        super().trigger(game)