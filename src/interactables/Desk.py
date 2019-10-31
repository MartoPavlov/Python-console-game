from src.interactables.Interactable import Interactable
from src.items.Item import Item
class Desk(Interactable):
    def __init__(self):
        Interactable.__init__(self, "desk", "You inspect the desk. All you see are papers.")
    
    def trigger(self, game):
        super().trigger(game)
        if self._active:
            print("...Wait a drawing of a cat..I think.")
            user = input("Enter action: ")
            if user.__eq__("take drawing"):
                print("You optained \'drawing\'")
                game.player.add_item(Item("drawing", "A drawing of a cat. On the other side you see \'8\'."))
                self._active = False
            elif user.__eq__("back"):
                print("Stepping back...")
            else:
                print("Notting happend.")