from src.interactables.Interactable import Interactable
class Drawer(Interactable):
    def __init__(self):
        Interactable.__init__(self, "drawer", "You inspect the drawer. It's filled with old\n"+
            "documents...I have no use for them.")

    def trigger(self, game):
        super().trigger(game) 