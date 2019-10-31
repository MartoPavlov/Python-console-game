from src.interactables.Interactable import Interactable
from src.items.Item import Item
class LockBox(Interactable):
    def __init__(self, color, passwd):
        Interactable.__init__(self, "box", "You come near the "+color+" box and see that there are 4\n"+
            "rotatable circles like the padlock in the basement.")
        self.__color = color
        self.__passwd = passwd

    def trigger(self, game):
        super().trigger(game)
        if self._active:
            user = input("Enter password: ")
            if len(user) == 4:
                if user.__eq__(self.__passwd):
                    print("It opened!")
                    print(f"You obtained \'{self.__color}-key\'")
                    game.player.add_item(Item(self.__color+"-key", "A key painted in "+self.__color+"."))
                    self._active = False
                elif user.__eq__("back"):
                    print("Wrong code..")
                else:
                    print("No effect.")
            else:
                print("You need 4-digit code. Example: \'4392\'")
        else:
            print("The box is empty.")