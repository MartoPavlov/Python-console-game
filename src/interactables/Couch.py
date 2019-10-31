from src.interactables.Interactable import Interactable
class Couch(Interactable):
    def __init__(self):
        Interactable.__init__(self, "couch", "You seat down...It is relaxing...")
    
    def trigger(self, game):
        super().trigger(game)