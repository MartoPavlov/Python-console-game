from src.interactables.Interactable import Interactable
class Radio(Interactable):
    def __init__(self, info):
        Interactable.__init__(self, "radio", info)
        
        def trigger(self, game):
            super().trigger(game)