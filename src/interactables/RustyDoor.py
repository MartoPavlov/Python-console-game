from src.interactables.Interactable import Interactable
class RustyDoor(Interactable):
    def __init__(self):
        Interactable.__init__(self, "door", "Locked.")
    
    def trigger(self, game):
        if self._active:
            user = input("Enter action: ")
            if user.__eq__("take out red-key"):
                if game.player.hasItem("red-key"):
                    print("It doesn't fit...but how?")
                else:
                    print("You don't have that item.")
            elif user.__eq__("take out key"):
                if game.player.hasItem("key"):
                    print("It opened!! Ha-ha very funny rusty key and red key...")
                    game.player.currRoom+=1
                    self._active = False
                else:
                    print("You don't have this item.")
            elif user.__eq__("back"):
                print("Action had no effect.")
            else:
                print("No effect.")
        else:
            print("The door opens..")