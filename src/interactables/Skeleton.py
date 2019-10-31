from src.interactables.Interactable import Interactable
from src.items.Item import Item
class Skeleton(Interactable):
    def __init__(self):
        Interactable.__init__(self, "skeleton", "You come to see the skeleton up close.\n"+
        "There is a number writen on the floor probably by the man as he was scratching\n"+
        "with his nails... at least when he had them. The number writen is \'1130\'.")
    
    def trigger(self, game):
        super().trigger(game)
        if self._active:
            print("You notice a key in his hand.")
            print("Tutorial: Sometimes while interacting with objects you can enter\n"+
                  "actions like \'take [ item name ]\' to take item or \'take out [item\n"+
                  "name]\' use item or \'back\' to cancel object inspection. Try to take\n"+
                  "the key:")
            user = input()
            if user.__eq__("take key"):
                game.player.add_item(Item("key", "Rusty iron key taken from the skeleton in the basement.\n"+
                    " The number \'6\' is engraved on it"))
                print("You optained \'key\'")
                self._active = False
                
            elif user.__eq__("back"):
                print("You step away from the skeleton.")
            else:
                print("Action is not possible.")   