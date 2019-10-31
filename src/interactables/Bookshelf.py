from src.interactables.Interactable import Interactable
from src.items.Item import Item
class Bookshelf(Interactable):
    def __init__(self):
        Interactable.__init__(self, "bookshelf", "There are many books here writen on a lenguage\n"+
                "I don't understand.")
        self.__counter = 0
    
    def trigger(self, game):
        super().trigger(game)
        while self._active:
            user = input("Enter action: ")
            if user.__eq__("take book"):
                print("You take a book")
                self.__counter+=1
                if self.__counter == 3:
                    game.player.add_item(Item("book #"+str(self.__counter), "The password is \'9217\'"))
                elif self.__counter == 5:
                    game.player.add_item(Item("book #"+str(self.__counter), "On every page you see the number \'7\'"))
                elif self.__counter == 20:
                    game.player.add_item(Item("book #"+str(self.__counter), "Notting interesting..."))
                    self._active = False
                else:
                    game.player.add_item(Item("book #"+str(self.__counter), "Notting interesting..."))
            elif user.__eq__("back"):
                break
            else:
                print("No effect...To go back type \'back\'")