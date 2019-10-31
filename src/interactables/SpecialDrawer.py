from src.interactables.Drawer import Drawer
from src.items.Item import Item
class SpecialDrawer(Drawer):
    def __init__(self):
        Drawer.__init__(self)
    
    def trigger(self, game):
        super().trigger(game)
        if self._active:
            print("Wait a second...")
            game.player.add_item(Item("grey-key", "A key painted in grey"))
            print("You optained \'grey-key\'")
            self._active = False