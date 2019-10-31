from src.interactables.Interactable import Interactable
class LampTable(Interactable):
    def __init__(self):
        Interactable.__init__(self, "table", "Coming to the table you see some letters\n"+
            "all across the table. You can't relate to any of them.")
    def trigger(self, game):
        super().trigger(game)