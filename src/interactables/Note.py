from src.interactables.Interactable import Interactable
class Note(Interactable):
    def __init__(self):
        Interactable.__init__(self, "note", "First number: number of couches so far.\n"+
            "Second number: number of chairs so far.\n"+
            "Third number: number of drawers so far.\n"+
            "Fourth number: number of colorful doors so far.")

    def trigger(self, game):
        super().trigger(game)