from src.interactables.Interactable import Interactable
class KeyDoor(Interactable):
    def __init__(self, color):
        Interactable.__init__(self, "door", "It's locked")
        self.__color = color

    def trigger(self, game):
        super().trigger(game)
        if self._active:
            user = input("Enter action: ")
            words = user.split()
            try:
                if words[0].__eq__("take") and words[1].__eq__("out"):
                    if words[2].__eq__(self.__color+"-key"): 
                        if game.player.hasItem(self.__color+"-key"):
                            print("The door opens. You enter the next room...")
                            game.player.currRoom+=1
                            self._active = False
                        else:
                            print("You don't have this item.")
                    elif words[2].__eq__("key"):
                        if game.player.hasItem("key"):
                            print("The key doesn't fit.")
                        else:
                            print("You don't have this item.")
                elif words[0].__eq__("back"):
                    print("Going back...")
                else:
                    print("Not possible")
            except IndexError:
                print("No effect")
        else:
            print("The door opens. You enter the next room...")
            game.player.currRoom+=1