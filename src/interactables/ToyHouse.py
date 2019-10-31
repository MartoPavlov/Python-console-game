from src.interactables.Interactable import Interactable
from src.items.Item import Item
class ToyHouse(Interactable):
    def __init__(self):
        Interactable.__init__(self, "toy-house", "You inspect the toy-house and see that you can open it's\n"+
                "half to reveal the inside. The house has one basement subfloor two floors\n"+
                "and one seiling floor. There is only one room with something in it. It has\n"+
                "a doll, a bed and a drawer all in small sizes")
        
    def trigger(self, game):
        super().trigger(game)

        user = input("Enter action: ")
        words = user.split()
        try:
            if words[0].__eq__("take"):
                if words[1].__eq__("doll"):
                    if game.player.hasItem("doll"):
                        print("You already have the doll")
                    else:
                        game.player.add_item(Item("doll", "Just a doll. Why I took it again?"))
                        print("You optained \'doll\'")
                elif words[1].__eq__("bed"):
                    if game.player.hasItem("bed"):
                        print("You already have the bed")
                    else:
                        game.player.add_item(Item("bed", "A toy bed. Under it you see \'2265\'"))
                        print("You optained \'bed\'")
                        self._active = False
                elif words[1].__eq__("drawer"):
                    if game.player.hasItem("drawer"):
                        print("You already have the drawer")
                    else:
                        game.player.add_item(Item("drawer", "A toy drawer. Under the drawer you see \'0\'."))
                        print("You optained \'drawer\'")
                else:
                    print("No such item.")
            elif words[0].__eq__("back"):
                print("You come back.")
            else:
                 print("No effect.")
        except IndexError:
            print("No effect")