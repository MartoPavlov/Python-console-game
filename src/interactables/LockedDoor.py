from src.interactables.Interactable import Interactable
class LockedDoor(Interactable):
    def __init__(self, passwd, near):
        Interactable.__init__(self, "door", "Door with a 4 digit padlock on it.")
        self.__passwd = passwd
        self.__near = near
    
    def trigger(self, game):
        if self._active:
            super().trigger(game)
            user = input("Enter password: ")
            if user.__eq__(self.__passwd):
                print("The padlock opens!")
                print("You open the door and go up the stares.");
                game.player.currRoom+=1
                self._active = False;
            elif user.__eq__(self.__near):
                print("It seems this is not the right combination");
            elif len(user) != 4:
                print("The password must be 4-digit code made from numbers 0-9")
            else:
                print("No effect.")
        else:
            print("The padlock opens!")
            print("You open the door and go up the stares.");
            game.player.currRoom+=1